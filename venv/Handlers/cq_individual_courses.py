from aiogram import types, F, Router
from texts.all_texts import individual_courses_text


router = Router()



@router.callback_query(F.data == 'individual_courses')
async def get_individual_courses(callback: types.CallbackQuery):
    await callback.message.answer(individual_courses_text,
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='Отзывы', url='https://t.me/pirogovka_now_otzivi')]]))
    await callback.answer()