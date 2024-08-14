from aiogram import Router, F, types
from texts.all_texts import letniy_intensiv_text, letniy_intensiv_2_text, komu_podhodit_text, temy_int
from all_contents import get_file
from Bot import bot
import os
from aiogram.types import LabeledPrice
from keyboards.menu_kb import get_kb_for_sub


router = Router()


def get_kb_leto():
    buttons = [[types.InlineKeyboardButton(text="О гайде", callback_data="letniy_intensiv")],
               [types.InlineKeyboardButton(text="Темы гайда", callback_data="Temy_intensiva")],
               [types.InlineKeyboardButton(text='Кому подходит гайд', callback_data='Komu_podhodit')],
               [types.InlineKeyboardButton(text='Купить (300р)', callback_data='!Oplata_letins')],
               [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@router.callback_query(F.data == 'letniy_intensiv')
async def get_contacts(callback: types.CallbackQuery):
    # await callback.message.answer_photo(photo=get_file('photo_5255942924443705185_y.jpg'),caption=letniy_intensiv_text)
    await callback.message.edit_text(letniy_intensiv_text)
    await callback.message.answer(text=letniy_intensiv_2_text, reply_markup=get_kb_leto())
    await callback.answer()

@router.callback_query(F.data == 'Temy_intensiva')
async def temy_letins(callback: types.CallbackQuery):
    await callback.message.edit_text(temy_int, reply_markup=get_kb_leto())
    await callback.answer()

@router.callback_query(F.data == 'Komu_podhodit')
async def komu_podhodit(callback: types.CallbackQuery):
    await callback.message.edit_text(komu_podhodit_text, reply_markup=get_kb_leto())
    await callback.answer()

# @router.callback_query(F.data == 'Oplata_letins')
# async def pay_leto(callback: types.CallbackQuery):
#      await bot.send_invoice(callback.from_user.id,
#                                title="Летний интенсив",
#                                description="Покупка летнего интенсива для медиков",
#                                provider_token=os.environ.get('paytoken'),
#                                currency="rub",
#                                prices=[LabeledPrice(label="Летний интенсив", amount=500 * 100)],
#                                payload="letins-invoice-payload")
#      await callback.message.edit_reply_markup(reply_markup=None)

# @router.message(PayFilter())
# async def successful_payment(message: types.Message):
#     if message.successful_payment.invoice_payload == 'letins-invoice-payload':
#         await message.answer('Здесь будет курс')

@router.callback_query(F.data == 'back_to_menu')
async def temy_letins(callback: types.CallbackQuery):
    await callback.message.edit_text('Выберите категорию', reply_markup=get_kb_for_sub())
    await callback.answer()