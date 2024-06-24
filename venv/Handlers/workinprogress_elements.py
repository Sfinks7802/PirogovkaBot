from aiogram import Router, F, types
from aiogram.filters import Command
from DataBase.db import find_user

router = Router()


@router.callback_query(F.data == 'gist_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.answer('В разработке...')
    await callback.answer()


@router.message(Command('check'))
async def chek_user(message: types.Message):
    print(find_user(message.from_user.id))
    await message.answer('nigger')
