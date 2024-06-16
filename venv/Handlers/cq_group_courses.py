from aiogram import types, F, Router
from texts.all_texts import groupe_courses_text


router = Router()



@router.callback_query(F.data == 'group_courses')
async def get_individual_courses(callback: types.CallbackQuery):
    await callback.message.answer(groupe_courses_text)
    await callback.answer()