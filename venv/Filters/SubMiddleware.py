from aiogram import BaseMiddleware, types
from aiogram.types import Message, TelegramObject, ChatMemberLeft
from PrivatInfo import bot
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub
from typing import Any, Callable, Dict, Awaitable


class SubMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=event.from_user.id)
        if isinstance(user_channel_status, ChatMemberLeft):
            await event.answer('Для использования бота подпишитесь на канал', reply_markup=get_keyboard_for_not_sub())
        else:
            return await handler(event, data)