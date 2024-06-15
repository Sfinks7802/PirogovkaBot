from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberLeft
from PrivatInfo import bot
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub
from keyboards.start_yes_sub_kb import get_kb_for_sub


router = Router()


@router.callback_query(F.data == 'sub_done')
async def check_sub(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=callback.from_user.id)
    if not isinstance(user_channel_status, ChatMemberLeft):
        await callback.message.answer('Спасибо')
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()


@router.message(Command('start'))
async def cmd_start(message: Message):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=message.from_user.id)
    if isinstance(user_channel_status, ChatMemberLeft):
        await message.answer('Для использования бота подпишитесь на канал', reply_markup=get_keyboard_for_not_sub())
    else:
        await message.answer('Добро пожаловать!',reply_markup=get_kb_for_sub())

