from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import okraski_txt
from aiogram.types import Message, FSInputFile
from all_contents import get_file


router = Router()



def new_cq(f_txt: str, cq_txt: str, pay_txt: str, msg_txt):
    @router.callback_query(F.data == f_txt)
    async def get_contacts(callback: types.CallbackQuery):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text=cq_txt, callback_data=pay_txt))
        builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
        await callback.message.answer(text=msg_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
        await callback.answer()

new_cq('test','тестовый платеж', '!okraski_pay', okraski_txt)