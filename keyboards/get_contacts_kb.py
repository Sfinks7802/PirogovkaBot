from aiogram import types


def get_contacts_kb():
    buttons = [[types.InlineKeyboardButton(text="Мой блог в ТГ", url='https://t.me/pirogovka_now')],
               [types.InlineKeyboardButton(text="Группа ВК", url='https://vk.com/student_mom_cafe')],
               [types.InlineKeyboardButton(text='Полезные видео', url='https://youtube.com/@pirogovka_now?si=86NMkWGQD5ceepjf')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard