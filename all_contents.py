from aiogram import types
from pathlib import Path
from aiogram.types import FSInputFile
from Bot import all_media_dir
import os

all_contents_names = {
    "Bilety_1-20": "Билеты 1-20 био.",
    "Bilety_21-40": "Билеты 21-40 био.",
    "Bilety_41-60": "Билеты 41-60 био.",
"Zadachi": "Задачи био.",
"Laboratornaya": "Лабораторная био.",
"Colok4": "Карточки хим. 4 колок",
"Colok5": "Карточки хим. 5 колок",
"Dyh_i_moch_colok": "Дых. и мочепол. колок",
"Dyh_conspect": "Дыхательная сис. конспект",
"Moch_conspect": "Мочевыделительная сис. конспект",

}


def get_kb_contents(contents):
    buttons = []
    for content in contents:
        buttons.append([types.InlineKeyboardButton(text=f'{all_contents_names[f"{content}"]}', callback_data=f'{content}')])
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_payed_content(content_name):
    return open(f'{content_name}.pdf' , 'rb')

# def get_photo():
#     with types.InputFile(Path(__file__).with_name('photo_5255942924443705185_y.jpg')) as photo:
#         return photo
# def get_file(filename, Path=Path):
#     return open(Path(__file__).with_name(filename))
# def get_photo():
#     return get_file('photo_5255942924443705185_y.jpg')

def get_file(name, subdir = None):
    if subdir is None:
     return FSInputFile(path=os.path.join(all_media_dir, name))
    else:
     return FSInputFile(path=os.path.join(all_media_dir, subdir, name))
