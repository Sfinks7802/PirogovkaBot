from datetime import datetime
from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import ai_for_med_2000_txt, ai_for_med_3000_txt

router = Router()


@router.callback_query(F.data == 'ai_for_med_buy_now')
async def get_intro( callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    if datetime.now() > datetime(2025, 11, 25): 
        builder.row(types.InlineKeyboardButton(text="💰 Взять комплект за 3000 ₽", callback_data='!ai_for_med_buy_now_3000'))
        await callback.message.answer(ai_for_med_3000_txt, reply_markup=builder.as_markup(), parse_mode='MarkdownV2')
    else:
        builder.row(types.InlineKeyboardButton(text="💰 Взять комплект за 2000 ₽ (до 25.11)", callback_data='!ai_for_med_buy_now_2000'))
        await callback.message.answer(ai_for_med_2000_txt, reply_markup=builder.as_markup(), parse_mode='MarkdownV2')
