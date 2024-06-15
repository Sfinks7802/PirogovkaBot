from aiogram import types


def get_kb_for_pay():
    button = [[types.InlineKeyboardButton(text="Отдать свои деньги", callback_data="pay_your_money")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard