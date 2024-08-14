from aiogram import BaseMiddleware, types
from aiogram.types import Message, TelegramObject, ChatMemberLeft, CallbackQuery
from Bot import bot
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub, get_keyboard_for_not_sub_bibla
from typing import Any, Callable, Dict, Awaitable


# class SubMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,
#             data: Dict[str, Any],
#     ) -> Any:
#         user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=event.from_user.id)
#         if isinstance(user_channel_status, ChatMemberLeft):
#             await bot.send_message(chat_id=event.from_user.id, text='Для использования бота подпишитесь на канал', reply_markup=get_keyboard_for_not_sub())
#         else:
#             return await handler(event, data)

text = '💎<i>Чтобы воспользоваться библиотекой, проверь, что ты подписан на @pirogovka_now и <u><a href="https://vk.com/kurs_202425">форум первокурсников РНИМУ</a></u></i>'
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