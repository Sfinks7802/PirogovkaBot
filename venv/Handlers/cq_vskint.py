from aiogram import Router, F, types
from keyboards.get_contacts_kb import get_contacts_kb
from texts.all_texts import vskint_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder
from all_contents import get_file


router = Router()


@router.callback_query(F.data == 'vskint')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!vskint_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer_photo(photo=get_file('vsk_int_photo.jpg'),caption=vskint_txt, reply_markup=builder.as_markup())
    await callback.answer()