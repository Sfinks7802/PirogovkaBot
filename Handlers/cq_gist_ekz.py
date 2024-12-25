from aiogram import Router, F, types
from texts.all_texts import gista_ekz_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'gist_ekz')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (3700р)", callback_data='!gist_ekz_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(gista_ekz_txt, reply_markup=builder.as_markup())
    await callback.answer()