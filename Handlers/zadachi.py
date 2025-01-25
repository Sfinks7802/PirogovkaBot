from aiogram import Router, F, types
from texts.all_texts import zadachi_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'zadachi')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!zadachi_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer(text=zadachi_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
    await callback.answer()
