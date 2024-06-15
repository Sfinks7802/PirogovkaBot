from aiogram import types


def get_keyboard_for_not_sub():
    buttons = [
        [types.InlineKeyboardButton(text="Оф. канал Telegram", url="https://t.me/pirogovka_now")],
        [types.InlineKeyboardButton(text="Я подписался", callback_data="sub_done")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard