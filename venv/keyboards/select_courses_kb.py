from aiogram import types


def get_kb_for_select_courses():
    buttons = [[types.InlineKeyboardButton(text="Химия", callback_data="himiya_courses")],
               [types.InlineKeyboardButton(text="Гистология", callback_data="gistologiya_courses")],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_select_gista_courses():
    buttons = [[types.InlineKeyboardButton(text="Индивидуальное", callback_data="individual_courses")],
               [types.InlineKeyboardButton(text="Групповое", callback_data="groupe_courses")],
               [types.InlineKeyboardButton(text="Назад", callback_data="courses")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard