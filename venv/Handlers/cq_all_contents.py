from aiogram import types, F, Router
from keyboards.select_courses_kb import get_kb_for_select_courses


router = Router()


@router.callback_query(F.data == 'all_contents')
async def all_contents( callback: types.CallbackQuery):

    await callback.answer()