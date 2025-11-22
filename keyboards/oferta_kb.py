from aiogram import types


def get_kb_for_oferta_agree(next_msg):
    buttons = [[types.InlineKeyboardButton(text="Согласен", callback_data=next_msg)]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard