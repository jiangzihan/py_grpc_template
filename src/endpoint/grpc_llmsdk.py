import asyncio
import signal
import logging
import os

import grpc
from grpc_reflection.v1alpha import reflection

from nlp.llmsdk_pb2 import DESCRIPTOR, Empty
from nlp.test1.test1_pb2 import MyStruct1
from nlp.llmsdk_pb2_grpc import HandlerServiceServicer, add_HandlerServiceServicer_to_server

class LoggingInterceptor(grpc.aio.ServerInterceptor):
    async def intercept_service(self, continuation, handler_call_details:grpc.HandlerCallDetails):
        print(f"Received request: {handler_call_details.method}")
        response:grpc.RpcMethodHandler = await continuation(handler_call_details)
        return response

class HandlerService(HandlerServiceServicer):

    def __init__(self):
        ...

    async def AddInbound(self, request:MyStruct1, context):
        print("进入: %s, b: %s"%(request.a, request.b))
        return Empty()


async def serve():

    # 1. 创建服务器
    server = grpc.aio.server(interceptors=[LoggingInterceptor()])

    # 2. 添加服务
    s1 = HandlerService()
    add_HandlerServiceServicer_to_server(s1, server)

    # 3. 添加反射服务
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name["HandlerService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    # 4. 关闭信号时执行
    async def shutdown(signal, loop):
        print(f'Received exit signal {signal.name}...')
        print('Closing database connection')
        print('Stopping gRPC server')
        await server.stop(grace=10)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(
            sig, lambda s=sig: asyncio.create_task(shutdown(s, loop)))

    # 5. 启动服务器
    host = os.environ.get("GRPC_LINSTEN")
    port = os.environ.get("GRPC_PORT")
    listen_addr = f"{host}:{port}"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()