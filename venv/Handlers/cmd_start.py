from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberLeft
from PrivatInfo import bot
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'sub_done')
async def send_random_value(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=callback.from_user.id)
    if not isinstance(user_channel_status, ChatMemberLeft):
        await callback.message.answer('Спасибо')


@router.message(Command('start'))
async def cmd_start(message: Message):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=message.from_user.id)
    if isinstance(user_channel_status, ChatMemberLeft):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Оф. канал Telegram",
            url="https://t.me/pirogovka_now"))
        builder.add(types.InlineKeyboardButton(
            text="Я подписался",
            callback_data="sub_done"))
        await message.answer('Для использования бота подпишитесь на канал', reply_markup=builder.as_markup())

