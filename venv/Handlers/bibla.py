from aiogram import Router, types, F
from aiogram.filters import Command
from texts.all_texts import bibla_text
from Filters.SubMiddleware import SubMiddlewareBibla

router = Router()
router.callback_query.middleware(SubMiddlewareBibla())

def get_kb_bibla():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", callback_data='bbAnat')],
               [types.InlineKeyboardButton(text="Гистология", callback_data='bbGist')],
               [types.InlineKeyboardButton(text="Биология", callback_data='bbBiol')],
               [types.InlineKeyboardButton(text="Латинский", callback_data='bbLat')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_bibla_Anat():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", callback_data='bbAnat')],
               [types.InlineKeyboardButton(text="Гистология", callback_data='bbGist')],
               [types.InlineKeyboardButton(text="Биология", callback_data='bbBiol')],
               [types.InlineKeyboardButton(text="Латинский", callback_data='bbLat')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_bibla_Gist():
    buttons = [[types.InlineKeyboardButton(text="Кафедральные методички", url='https://drive.google.com/drive/folders/1HwhbBdVbt_gSj00wp-60fIF0VkNYTOuV?usp=drive_link')],
               [types.InlineKeyboardButton(text="Неофиц. методы", url='https://drive.google.com/drive/folders/1-2Ha3Ji0Bqdf3NubXJN5hcV-tlKyyX0x?usp=drive_link')],
               [types.InlineKeyboardButton(text="Учебники и атласы", url='https://drive.google.com/drive/folders/1D-H9W9yCYSEryZLTun7RPVhZVHNTLhgn?usp=drive_link')],
               [types.InlineKeyboardButton(text='Назад', callback_data='bibla')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_bibla_Lat():
    buttons = [[types.InlineKeyboardButton(text="База на тест", url='https://drive.google.com/drive/folders/1ZQhGks0V6nlXl37YzFU_NMF-rmhk64ai?usp=drive_link')],
               [types.InlineKeyboardButton(text="Письменная часть", url='https://drive.google.com/drive/folders/1A7LqHAETwgUJJ8gl4PEXVcGWM9ZMfskj?usp=drive_link')],
               [types.InlineKeyboardButton(text="Рабочая тетрадь", url='https://drive.google.com/drive/folders/1egGm49sn10bqYqXJq8vrf1tMCBdJFdnC?usp=drive_link')],
               [types.InlineKeyboardButton(text="Устная часть", url='https://drive.google.com/drive/folders/1sc24Vz-WbJoqUQXPfrGIMxWbH5Du0_Y4?usp=drive_link')],
               [types.InlineKeyboardButton(text="Учебник", url='https://drive.google.com/drive/folders/1xBfG9CFJwcvTizVc7kr3muyc2Dml-Stv?usp=drive_link')],
               [types.InlineKeyboardButton(text='Назад', callback_data='bibla')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_bibla_Biol():
    buttons = [[types.InlineKeyboardButton(text="Доп. конспекты, файлы, таблицы", url='https://drive.google.com/drive/folders/1-Ky4FTIN4xuBpl_Fo5PT_9wWoO8PZWx0?usp=drive_link')],
               [types.InlineKeyboardButton(text="Лабы", url='https://drive.google.com/drive/folders/1-GhPQqSk5dOml8XA46w-xrFkIUjnwiaS?usp=drive_link')],
               [types.InlineKeyboardButton(text="Методички", url='https://drive.google.com/drive/folders/1ux8zwt6GYvDq6SiOiJ6cQSYoEm9eo-v5?usp=drive_link')],
               [types.InlineKeyboardButton(text="Ответы на коллки и тесты", url='https://drive.google.com/drive/folders/1-JUi3fzn7Wngr-j8m9A3vWCQpuM2lNiO?usp=drive_link')],
               [types.InlineKeyboardButton(text="Учебники", url='https://drive.google.com/drive/folders/1nVP1I8tF6EwmYOzLKAB-_SrQbOJUf57q?usp=drive_link')],
               [types.InlineKeyboardButton(text="Тетради с ответами", url='https://drive.google.com/drive/folders/1Dw3Vz2iN52DSPMYHELud0FZBCTrH2ri4?usp=drive_link')],
               [types.InlineKeyboardButton(text="Экзамен", url='https://drive.google.com/drive/folders/1-Gu_BLGjah9bw75TpTrOWHyvc6IjThJh?usp=drive_link')],
               [types.InlineKeyboardButton(text="Ярыгин", url='https://drive.google.com/drive/folders/1onQEkrBSm00j0UO66QHVi5JE3GhDNiDO?usp=drive_link')],
               [types.InlineKeyboardButton(text='Назад', callback_data='bibla')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == 'bibla')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(bibla_text, reply_markup=get_kb_bibla(), parse_mode='HTML')
    await callback.answer()