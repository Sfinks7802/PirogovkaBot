from datetime import datetime
from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import conf_for_med_txt

router = Router()


@router.callback_query(F.data == 'conf_for_med_buy_now')
async def get_intro( callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Цена по акции — 500 ₽ (вместо 1000 ₽)", callback_data='!conf_for_med_buy_now'))
    await callback.message.answer(conf_for_med_txt, reply_markup=builder.as_markup(), parse_mode='MarkdownV2')
