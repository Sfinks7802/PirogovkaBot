from aiogram import Router, F, types
from texts.all_texts import cnsint_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'cnsint')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (1000р)", callback_data='!cnsint_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(cnsint_txt, reply_markup=builder.as_markup())
    await callback.answer()