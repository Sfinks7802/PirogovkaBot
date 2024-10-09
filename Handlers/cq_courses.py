from aiogram import types, F, Router
from keyboards.select_courses_kb import get_kb_for_select_gista_courses, get_kb_for_select_courses
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import (himiya_courses_txt, anatrepit_txt)


router = Router()


@router.callback_query(F.data == 'courses')
async def get_courses( callback: types.CallbackQuery):
    await callback.message.edit_text('Выбери предмет, который тебя интересует \n'
'У нас есть проверенные репетиторы пока только по 3-м предметам 🔥', reply_markup=get_kb_for_select_courses())
    await callback.answer()


@router.callback_query(F.data == 'himiya_courses')
async def get_courses( callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Офф. канал", url="https://t.me/chemmm_rsmu"))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='courses'))
    await callback.message.edit_text(himiya_courses_txt, reply_markup=builder.as_markup())
    await callback.answer()

@router.callback_query(F.data == 'anatomiya_courses')
async def get_courses( callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='courses'))
    await callback.message.edit_text(anatrepit_txt, reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == 'gistologiya_courses')
async def get_courses( callback: types.CallbackQuery):
    await callback.message.edit_text('Выбери формат занятий', reply_markup=get_kb_for_select_gista_courses())
    await callback.answer()