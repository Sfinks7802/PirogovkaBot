from aiogram import types

 
def get_kb_for_sub():
    buttons = [[types.InlineKeyboardButton(text="Библиотека студента", callback_data="bibla")],
                [types.InlineKeyboardButton(text='Гайд по учебе', callback_data='letniy_intensiv')],
               # [types.InlineKeyboardButton(text='Габе', callback_data='!qwerty')],
               [types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
               [types.InlineKeyboardButton(text='Контакты', callback_data='contacts')],
               # [types.InlineKeyboardButton(text='Занятия', callback_data='courses')],
               # [types.InlineKeyboardButton(text='Мои материалы', callback_data='my_materials')],
               [types.InlineKeyboardButton(text='Конспекты_Пироговка', callback_data='all_contents')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard