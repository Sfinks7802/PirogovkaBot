from aiogram import types


def get_kb_for_select_courses():
    buttons = [[types.InlineKeyboardButton(text="Индивиудальные занятия", callback_data="individual_courses")],
               [types.InlineKeyboardButton(text="Групповые занятия", callback_data="group_courses")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard