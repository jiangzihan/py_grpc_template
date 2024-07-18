import os
from grpc_tools import protoc  # type: ignore

# build main service
def main_service():
    PROTO_DIR = "./protos"
    OUTPUT_DIR = "."

    protoc.main((
        '',
        f'-I={PROTO_DIR}',
        f'--python_out={OUTPUT_DIR}',
        f'--grpc_python_out={OUTPUT_DIR}',
        f'--pyi_out={OUTPUT_DIR}',
        f'{PROTO_DIR}/nlp/llmsdk.proto',
        f'{PROTO_DIR}/nlp/test1/test1.proto',
    ))


# other request service
def external_service():
    PROTO_DIR = "./protos"
    OUTPUT_DIR = "."

    protoc.main((
        '',
        f'-I={PROTO_DIR}',
        f'--python_out={OUTPUT_DIR}',
        f'--grpc_python_out={OUTPUT_DIR}',
        f'--pyi_out={OUTPUT_DIR}',
        f'{PROTO_DIR}/user_center/user_center.proto',
    ))

if __name__ == "__main__":
    main_service()
    external_service()