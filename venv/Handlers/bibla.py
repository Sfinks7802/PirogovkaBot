from aiogram import Router, types, F
from aiogram.filters import Command
from texts.all_texts import bibla_text
from Filters.SubMiddleware import SubMiddlewareBibla

router = Router()
# router.callback_query.middleware(SubMiddlewareBibla())
def get_kb_bibla():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", callback_data='bbAnat')],
               [types.InlineKeyboardButton(text="Гистология", callback_data='bbGist')],
               [types.InlineKeyboardButton(text="Биохимия", url='https://drive.google.com/drive/folders/1-od7myWaZzJusSeZ1mqdioXkAN-67_m6?usp=sharing')],
               [types.InlineKeyboardButton(text="Микробиология", url='https://drive.google.com/drive/folders/1-oXxV2FgVB5i19M7CWKxzbOE51uSbS_N?usp=sharing')],
               [types.InlineKeyboardButton(text="Физиология", url='https://drive.google.com/drive/folders/1-SD-2Z72d_s9IY-KqV23RYJBmLeOsnTw?usp=sharing')],
               [types.InlineKeyboardButton(text="Биология", callback_data='bbBiol')],
               [types.InlineKeyboardButton(text="Латинский", callback_data='bbLat')],
               [types.InlineKeyboardButton(text="Химия", callback_data='bbHim')],
               [types.InlineKeyboardButton(text="Физика", callback_data='bbPhyz')],
               [types.InlineKeyboardButton(text="Биоэтика", url='https://drive.google.com/drive/folders/1-q67GrVtQgG_ZjtB27YZQMtHoyH0KClP?usp=sharing')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_bibla_Anat():
    buttons = [[types.InlineKeyboardButton(text="Дых. и мочепол. сис.", url='https://drive.google.com/drive/folders/1ruFVLCrXpsbzm2nAGUWeERnSB4i9X1oy?usp=drive_link')],
               [types.InlineKeyboardButton(text="Миология", url='https://drive.google.com/drive/folders/1POdJLASUwOdvclVJu8-VkQlZaPDdeT5v?usp=drive_link')],
               [types.InlineKeyboardButton(text="Остеология", url='https://drive.google.com/drive/folders/1dp7BoCnx0txjhW25Lkr1jfjHGQ5iU0Ne?usp=drive_link')],
               [types.InlineKeyboardButton(text="Пищевар. сис.", url='https://drive.google.com/drive/folders/1mvisp6Sy1d0T5RC3JWx_MzK_-exkOtPx?usp=drive_link')],
               [types.InlineKeyboardButton(text="ПНС", url='https://drive.google.com/drive/folders/1tj2yk3VaPNSmqhqZRQ9QKaYY24ACCe1F?usp=drive_link')],
               [types.InlineKeyboardButton(text="Синдесмология", url='https://drive.google.com/drive/folders/1CvvLK9ihH6ym8jwhKX94Hv2VJfBHY921?usp=drive_link')],
               [types.InlineKeyboardButton(text="ССС", url='https://drive.google.com/drive/folders/1IRJQtHdg7iXq8k2WWEDKe4pUn_6WLXyq?usp=drive_link')],
               [types.InlineKeyboardButton(text="Учебники", url='https://drive.google.com/drive/folders/1tEP_D_TYIQN-r4wmQqoT-1xnCKgg4yy8?usp=drive_link')],
               [types.InlineKeyboardButton(text="ЦНС", url='https://drive.google.com/drive/folders/11WKo85IvGt9yDNgf3jAo7-Y7L2eiod4k?usp=drive_link')],
               [types.InlineKeyboardButton(text="Экзамен", url='https://drive.google.com/drive/folders/1kO0xoSDhbTy9O9jbzxmJM1oK5ogdPAx9?usp=drive_link')],
               [types.InlineKeyboardButton(text="Эндокринная сис.", url='https://drive.google.com/drive/folders/1Jc148PNQEW2GFGBNDVrRT-eiZhj713Kk?usp=drive_link')],
               [types.InlineKeyboardButton(text="Эстезиология. Черепные нервы", url='https://drive.google.com/drive/folders/1qyqXZ7biWVpimHW4C2cnwH16oMWG7mDq?usp=drive_link')],
               [types.InlineKeyboardButton(text='Назад', callback_data='bibla')]]
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


def get_kb_bibla_Phyz():
    buttons = [[types.InlineKeyboardButton(text="База", url='https://drive.google.com/drive/folders/1-DKvWlNkJXE5npIXwIWpl4bLBaeujDfu?usp=sharing')],
               [types.InlineKeyboardButton(text="Второй коллок", url='https://drive.google.com/drive/folders/1-NnS_lV0ATQIeC-bS6ekneg6IFNlitla?usp=sharing')],
               [types.InlineKeyboardButton(text="Лабы", url='https://drive.google.com/drive/folders/1-FY0dY342GQspbbmd9vsQ4yeLVrdg4QW?usp=sharing')],
               [types.InlineKeyboardButton(text="Первый коллок", url='https://drive.google.com/drive/folders/1-LlEBTdF8SPuo7Lni6dfjkQHey7Fl29z?usp=sharing')],
               [types.InlineKeyboardButton(text="Третий коллок", url='https://drive.google.com/drive/folders/1-Nwipec0ijUrk_s_z4pWYJm8O08Vbsa9?usp=sharing')],
               [types.InlineKeyboardButton(text="Учебники", url='https://drive.google.com/drive/folders/1-BUcCS8aE4UadfO38FZaE-KT7xZrpVux?usp=sharing')],
               [types.InlineKeyboardButton(text="Четвертый коллок", url='https://drive.google.com/drive/folders/1-TaJDxjBBcMohM3CVRReNvqoJqUIABlu?usp=sharing')],
               [types.InlineKeyboardButton(text="Конспекты", url='https://drive.google.com/file/d/1noRsAa_Ri1jsW2Oe-YOz8pFGWgZSlMFv/view?usp=sharing')],
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


def get_kb_bibla_Him():
    buttons = [[types.InlineKeyboardButton(text="1 колок", url='https://drive.google.com/drive/folders/1DBzrua9-YQ9U-sASXjheGFH24tRD-B8e?usp=sharing')],
               [types.InlineKeyboardButton(text="2 колок", url='https://drive.google.com/drive/folders/1G6bqv3Lvy7oPE97OG24Pv41LCYM8lVrv?usp=drive_link')],
               [types.InlineKeyboardButton(text="3 колок", url='https://drive.google.com/drive/folders/18zOi58bXrVsP375LsidLY8jcmU-fKjL_?usp=drive_link')],
               [types.InlineKeyboardButton(text="4 колок", url='https://drive.google.com/drive/folders/1CnFc6moIdKh-dAq-TVNIZFtBxEgcR26Z?usp=drive_link')],
               [types.InlineKeyboardButton(text="5 колок", url='https://drive.google.com/drive/folders/1N5NrlStMLQO9IKWIzS0DYUm5iv344A0c?usp=drive_link')],
               [types.InlineKeyboardButton(text="6 колок", url='https://drive.google.com/drive/folders/1_MA42UUJxmO86VIeUWAHX6idVWoNCRkU?usp=drive_link')],
               [types.InlineKeyboardButton(text="Учебники/методы", url='https://drive.google.com/drive/folders/1EGABcvxpqkIPxuZJHqzcOX664Ng72GYH?usp=drive_link')],
               [types.InlineKeyboardButton(text="ЭКЗАМЕН", url='https://drive.google.com/drive/folders/1zK7vCc68AgOW1_3iO3zNqEqe0-cc40DD?usp=drive_link')],
               [types.InlineKeyboardButton(text='Назад', callback_data='bibla')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == 'bibla')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(bibla_text, reply_markup=get_kb_bibla(), parse_mode='HTML')
    await callback.answer()

@router.callback_query(F.data == 'bbAnat')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Anat())

@router.callback_query(F.data == 'bbGist')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Gist())

@router.callback_query(F.data == 'bbBiol')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Biol())

@router.callback_query(F.data == 'bbLat')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Lat())

@router.callback_query(F.data == 'bbHim')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Him())

@router.callback_query(F.data == 'bbPhyz')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_bibla_Phyz())