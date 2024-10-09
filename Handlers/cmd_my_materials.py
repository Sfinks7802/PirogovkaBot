from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from DataBase.db import get_contents
from all_contents import get_kb_contents


router = Router()


@router.message(Command('my_matirials'))
async def my_contents(message: Message):
    try:
        content_list = get_contents(message.from_user.id)
        await message.answer("Выберите файл", reply_markup=get_kb_contents(content_list))
    except TypeError:
        await message.answer('У вас нет сохраненных материалов')


@router.callback_query(F.data == 'my_materials')
async def my_contents(callback: CallbackQuery):
    try:
        content_list = get_contents(callback.from_user.id)
        await callback.message.answer("Выберите файл", reply_markup=get_kb_contents(content_list))
        await callback.answer()
    except TypeError:
        await callback.message.answer('У вас нет сохраненных материалов')
        await callback.answer()
