import unittest

from src.data_request.local_pool import connect, request_cli1

class Tests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        from dotenv import load_dotenv
        load_dotenv()
        return None

    async def test_test1(self):
        await connect()
        for i in range(3):
            print("第 %d 请求"%i)
            await request_cli1(a="ac",b=123)
