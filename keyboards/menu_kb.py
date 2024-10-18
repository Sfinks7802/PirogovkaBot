from aiogram import types

 
def get_kb_for_sub():
    buttons = [[types.InlineKeyboardButton(text="Эксклюзивно РНИМУ", callback_data="bibla")],
               # [types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
               [types.InlineKeyboardButton(text='Репетиторы', callback_data='courses')],
               [types.InlineKeyboardButton(text='Материалы от Пироговки', callback_data='Pirogovka_matirials')]]
               # [types.InlineKeyboardButton(text='Мои материалы', callback_data='my_materials')],
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_Pirogovka_matirials():
    buttons = [
        # [types.InlineKeyboardButton(text='Гайд по учебе', callback_data='letniy_intensiv')],
        [types.InlineKeyboardButton(text='Контакты', callback_data='contacts')],
        [types.InlineKeyboardButton(text='Конспекты', callback_data='pirogovka_conspects')],
        [types.InlineKeyboardButton(text='Вспомнить всё 4', callback_data='vskint')],
        [types.InlineKeyboardButton(text='Вспомнить всё 5', callback_data='remember5')],
        [types.InlineKeyboardButton(text='Вспомнить всё 1', callback_data='remember1')],
        [types.InlineKeyboardButton(text='Интенсив ЦНС', callback_data='cnsint')],
        [types.InlineKeyboardButton(text='Чеклист по покупкам', callback_data='checklist')],
        [types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
        # [types.InlineKeyboardButton(text='Конспекты_Пироговка', callback_data='all_contents')],
        [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_pirogovka_conspects():
    buttons = [
        [types.InlineKeyboardButton(text='Конспект сердечно-сосуд. сис.', callback_data='SerSod_conspect')],
        [types.InlineKeyboardButton(text='Анатомия. Черепно-мозговые нервы', callback_data='anatint')],
        [types.InlineKeyboardButton(text='Эмбриогенез', callback_data='Embriogenez_conspect')],
        [types.InlineKeyboardButton(text='Назад', callback_data='Pirogovka_matirials')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

