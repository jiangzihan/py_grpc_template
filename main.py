import asyncio
from dotenv import load_dotenv

from src.endpoint.grpc_llmsdk import serve

async def main():
    await serve()

if __name__=="__main__":
    load_dotenv()
    asyncio.run(main())