from aiogram import Router, types, F
from aiogram.filters import Command
from texts.all_texts import bibla_text

router = Router()


def get_kb_bibla():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", url='https://drive.google.com/drive/folders/1lVHB8J1H9cKH7h3QuC6AplpYtT1KXmE6?usp=sharing')],
               [types.InlineKeyboardButton(text="Гистология", url='https://drive.google.com/drive/folders/1FN8Gmtliu8E-xWJpSCERZo3_5sIhazft?usp=sharing')],
               [types.InlineKeyboardButton(text="Биология", url='https://drive.google.com/drive/folders/1sQS6oQX8-ZIkdTh27AfT3CtNVqWm74JH?usp=sharing')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

text = '💎<i>Чтобы воспользоваться библиотекой, проверь, что ты подписан на @pirogovka_now и <u><a href="https://vk.com/kurs_202425">форум первокурсников РНИМУ</a></u></i>'
@router.callback_query(F.data == 'bibla')
async def get_menu(callback: types.CallbackQuery):
    await callback.message.answer(bibla_text, reply_markup=get_kb_bibla(), parse_mode='HTML')
    await callback.message.answer(text, parse_mode='HTML')
    await callback.answer()