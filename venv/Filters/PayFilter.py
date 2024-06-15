from aiogram.filters import BaseFilter
from aiogram.types import Message

class PayFilter(BaseFilter):
    async def __call__(self, message: Message):
        if message.successful_payment:
            return True
        else:
            return False