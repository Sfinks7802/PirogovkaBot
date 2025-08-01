from aiogram import BaseMiddleware, types
from aiogram.types import Message, TelegramObject, ChatMemberLeft, CallbackQuery
from Bot import bot
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub, get_keyboard_for_not_sub_bibla
from typing import Any, Callable, Dict, Awaitable


class SubMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=event.from_user.id)
        if isinstance(user_channel_status, ChatMemberLeft):
            await bot.send_message(chat_id=event.from_user.id, text='Для поучения памятки вступи в <a href=''группу', reply_markup=get_keyboard_for_not_sub())
        else:
            return await handler(event, data)

text = '💎<i>Чтобы воспользоваться библиотекой, проверь, что ты подписан на @pirogovka_now и <u><a href="https://vk.com/pirogovka_now">форум первокурсников РНИМУ</a></u></i>'
class SubMiddlewareBibla(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user_channel_status_1 = await bot.get_chat_member(chat_id='-1002209887331', user_id=event.from_user.id)
        user_channel_status_2 = await bot.get_chat_member(chat_id='-1001841308905', user_id=event.from_user.id)
        if isinstance(user_channel_status_1, ChatMemberLeft) or isinstance(user_channel_status_2, ChatMemberLeft):
            await bot.send_message(chat_id=event.from_user.id, text=text, reply_markup=get_keyboard_for_not_sub_bibla())
        else:
            return await handler(event, data)


from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):  # [1]
    def __init__(self, chat_type: Union[str, list]): # [2]
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
