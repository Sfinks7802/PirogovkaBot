from Bot import bot
from aiogram import Router
from Filters.SubMiddleware import ChatTypeFilter
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


async def generate_link(chat_id, times=1):
    link = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=times)
    return link.invite_link

@router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), Command(commands=['get_link']))
async def get_chat_id(message: Message):
    link = await generate_link(message.chat.id)
    await message.answer(f'{link}')
    await bot.send_message(chat_id=1222017921, text=f'{message.chat.id} \n {message.chat.title}')


