from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberLeft
from PrivatInfo import bot


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=message.from_user.id)
    if isinstance(user_channel_status, ChatMemberLeft):
        await message.answer('text if not in group')