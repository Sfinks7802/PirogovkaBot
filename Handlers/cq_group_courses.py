from aiogram import types, F, Router
from texts.all_texts import groupe_courses_text
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()



@router.callback_query(F.data == 'groupe_courses')
async def get_individual_courses(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='gistologiya_courses'))
    await callback.message.edit_text(groupe_courses_text, reply_markup=builder.as_markup())
    await callback.answer()