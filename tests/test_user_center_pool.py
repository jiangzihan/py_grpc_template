import unittest

from src.data_request.user_center_pool import connect, new_captcha

class Tests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        from dotenv import load_dotenv
        load_dotenv()
        return None

    async def test_test1(self):
        await connect()
        text = await new_captcha()
        print(text)