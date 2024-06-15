from aiogram import types


def get_kb_for_sub():
    buttons = [[types.InlineKeyboardButton(text="Отдать свои деньги", callback_data="pay_your_money")],
               [types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard