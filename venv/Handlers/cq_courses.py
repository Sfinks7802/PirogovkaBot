from aiogram import types, F, Router
from keyboards.select_courses_kb import get_kb_for_select_courses


router = Router()


@router.callback_query(F.data == 'courses')
async def get_courses( callback: types.CallbackQuery):
    await callback.message.answer('Пожалуйста, выберите интересующий вас формат занятий', reply_markup=get_kb_for_select_courses())
    await callback.answer()