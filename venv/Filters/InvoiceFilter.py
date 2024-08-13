from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class InvoiceFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data[0] == '!':
            return True
        else:
            return False