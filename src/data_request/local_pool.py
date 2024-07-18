import os
import asyncio
from grpc import aio
from nlp.llmsdk_pb2 import Empty
from nlp.llmsdk_pb2_grpc import HandlerServiceStub
from nlp.test1.test1_pb2 import MyStruct1

class GRPCClientPool:
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
        stub = HandlerServiceStub(channel)
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

host = "127.0.0.1"
port = os.environ.get("GRPC_PORT", 50051)
target = f"{host}:{port}"
LLMSDK_GRPC_POOL = GRPCClientPool(target=target, pool_size=5)


### from .pool import LLMSDK_GRPC_POOL
### client = await LLMSDK_GRPC_POOL.get_client()
### response:Empty = await client.AddInbound(MyStruct1(a=a,b=b))
async def connect():
    global LLMSDK_GRPC_POOL
    await LLMSDK_GRPC_POOL.initialize_pool()


# test1
async def request_cli1(a:str,b:int) -> None:
    client = await LLMSDK_GRPC_POOL.get_client()
    response:Empty = await client.AddInbound(
        MyStruct1(a=a,b=b)
    )
    print("AIO client received: %s"%response)
