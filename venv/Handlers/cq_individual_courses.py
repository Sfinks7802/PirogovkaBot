from aiogram import types, F, Router
from texts.all_texts import individual_courses_text, for_who_is_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()



@router.callback_query(F.data == 'individual_courses')
async def get_individual_courses(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Для кого", callback_data='for_who_is'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='gistologiya_courses'))
    await callback.message.edit_text(individual_courses_text, reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == 'for_who_is')
async def get_individual_courses(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='individual_courses'))
    await callback.message.edit_text(for_who_is_txt, reply_markup=builder.as_markup())
    await callback.answer()