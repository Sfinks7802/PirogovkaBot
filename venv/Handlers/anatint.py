from aiogram import Router, F, types
from texts.all_texts import anatint_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'anatint')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (400р)", callback_data='!anatint_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(anatint_txt, reply_markup=builder.as_markup())
    await callback.answer()