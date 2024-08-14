from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from all_contents import get_file


router = Router()


@router.message(Command('test'))
async def get_menu(message: types.Message):
    await message.answer_photo(photo=get_file('photo_5255942924443705185_y.jpg'))