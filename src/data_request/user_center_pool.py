import os
import asyncio
from grpc import aio
from user_center.user_center_pb2 import Empty, NewCaptchaResponse
from user_center.user_center_pb2_grpc import UserCenterServiceStub


class UserCenterServicePool:
    def __init__(self, target, pool_size):
        self.target = target
        self.pool_size = pool_size
        self.pool = asyncio.Queue(maxsize=pool_size)
        self.lock = asyncio.Lock()

    async def initialize_pool(self):
        if self.pool.qsize() == 0:
            for i in range(self.pool_size):
                await self.pool.put(await self._create_client())

    async def _create_client(self):
        CHANNEL_OPTIONS = [
            ("grpc.lb_policy_name", "pick_first"),
            ("grpc.enable_retries", 0),
            ("grpc.keepalive_timeout_ms", 10000),
        ]
        channel = aio.insecure_channel(self.target,options=CHANNEL_OPTIONS)
        stub = UserCenterServiceStub(channel)
        return stub

    async def get_client(self):
        async with self.lock:
            if self.pool.empty():
                return await self._create_client()
            return await self.pool.get()

    async def release_client(self, client):
        async with self.lock:
            await self.pool.put(client)

    async def close(self):
        while not self.pool.empty():
            client = await self.pool.get()
            await client._channel.close()

    async def __aenter__(self):
        await self.initialize_pool()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

host = os.environ.get("USERCENTER_GRPC_HOST")
port = os.environ.get("USERCENTER_GRPC_PORT")
target = f"{host}:{port}"
USERCENTER_GRPC_POOL = UserCenterServicePool(target=target, pool_size=5)

async def connect():
    global USERCENTER_GRPC_POOL
    await USERCENTER_GRPC_POOL.initialize_pool()



async def new_captcha() -> str:
    client = await USERCENTER_GRPC_POOL.get_client()
    params = Empty()
    response:NewCaptchaResponse = await client.NewCaptcha(params)
    print("%s"%response)
    return response.text
