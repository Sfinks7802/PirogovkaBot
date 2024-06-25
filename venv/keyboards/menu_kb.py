from aiogram import types

 
def get_kb_for_sub():
    buttons = [[types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
               [types.InlineKeyboardButton(text='Контакты', callback_data='contacts')],
               [types.InlineKeyboardButton(text='Занятия', callback_data='courses')],
               [types.InlineKeyboardButton(text='Мои материалы', callback_data='my_materials')],
               [types.InlineKeyboardButton(text='Все материалы', callback_data='all_contents')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard