from aiogram import Router, F, types
from texts.all_texts import okraski_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'okraski')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!okraski_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer(text=okraski_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
    await callback.answer()
