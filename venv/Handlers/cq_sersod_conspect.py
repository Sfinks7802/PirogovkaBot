from aiogram import Router, F, types
from texts.all_texts import sersod_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'SerSod_conspect')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!SerSod_conspect_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(sersod_txt, reply_markup=builder.as_markup())
    await callback.answer()