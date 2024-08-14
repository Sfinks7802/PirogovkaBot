from aiogram import types


def get_keyboard_for_not_sub():
    buttons = [
        [types.InlineKeyboardButton(text="Оф. канал Telegram", url="https://t.me/pirogovka_now")],
        [types.InlineKeyboardButton(text="Я подписался", callback_data="sub_done")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_keyboard_for_not_sub_bibla():
    buttons = [
        [types.InlineKeyboardButton(text="Оф. канал Telegram", url="https://t.me/pirogovka_now")],
        [types.InlineKeyboardButton(text="Группа ВК", url="https://vk.com/kurs_202425")],
        [types.InlineKeyboardButton(text="Я подписался", callback_data="sub_done_bibla")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard