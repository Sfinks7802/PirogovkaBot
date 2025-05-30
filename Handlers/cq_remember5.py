from aiogram import Router, F, types
from texts.all_texts import remember5_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'remember5')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!remember5_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(remember5_txt, reply_markup=builder.as_markup())
    await callback.answer()