from aiogram import Router, types
from aiogram.filters import Command
from keyboards.menu_kb import get_kb_for_sub


router = Router()


@router.message(Command('menu'))
async def get_menu(message: types.Message):
    await message.answer('Выберите категорию', reply_markup=get_kb_for_sub())