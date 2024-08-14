from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from all_contents import get_file
from texts.all_texts import (gista_course_txt, for_who_txt, how_learn_txt, why_us_txt, mission_txt,
                             tarifs_course_txt, courator_txt, conspects_course_txt)

router = Router()


def get_kb_for_gista_course():
    buttons = [[types.InlineKeyboardButton(text='О курсе', callback_data='back_to_gista_course')],
               [types.InlineKeyboardButton(text="Для кого этот курс", callback_data="for_who")],
               [types.InlineKeyboardButton(text='Конспекты', callback_data='conspects_course')],
               [types.InlineKeyboardButton(text='Как проходит обучение', callback_data="how_learn")],
               [types.InlineKeyboardButton(text='Почему лучше с куратором', callback_data='courator')],
               [types.InlineKeyboardButton(text='Почему мы', callback_data='why_us')],
               [types.InlineKeyboardButton(text='Миссия этого курса', callback_data='mission_course')],
               [types.InlineKeyboardButton(text='ТАРИФЫ', callback_data='tarifs_course')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_tarifs():
    buttons = [[types.InlineKeyboardButton(text="Купить", callback_data="buy_gista_course")],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_gista_course')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_for_buy_gista_course():
    buttons = [[types.InlineKeyboardButton(text="Я сам", callback_data="!with_yourself_gista_course")],
               [types.InlineKeyboardButton(text='С куратором', callback_data='!with_courator_gista_course')],
               [types.InlineKeyboardButton(text='С автором курса', callback_data='!with_auther_gista_course')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_gista_course')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@router.callback_query(F.data == 'gist_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(gista_course_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()


# @router.message(CommandStart(deep_link=True, magic=F.args == 'gist_course'))
# async def get_guist_course(message: types.Message):
#     await message.answer(gista_course_txt, reply_markup=get_kb_for_gista_course())


@router.message(Command('check'))
async def chek_user(message: types.Message):
    print(find_user(message.from_user.id))
    await message.answer('nigger')


@router.callback_query(F.data == 'for_who')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(for_who_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'conspects_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(conspects_course_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'how_learn')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(how_learn_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'courator')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(courator_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'why_us')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(why_us_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'mission_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(mission_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'tarifs_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(tarifs_course_txt, reply_markup=get_kb_for_tarifs())
    await callback.answer()

@router.callback_query(F.data == 'back_to_gista_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(gista_course_txt, reply_markup=get_kb_for_gista_course())
    await callback.answer()

@router.callback_query(F.data == 'buy_gista_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.edit_text(tarifs_course_txt, reply_markup=get_kb_for_buy_gista_course())
    await callback.answer()