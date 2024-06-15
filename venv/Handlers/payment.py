from aiogram import Router, types, F
from Filters.payfilter import PayFilter
from aiogram.types import Message, LabeledPrice
from PrivatInfo import bot, paytoken
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'pay_your_money')
async def pay_money(callback: types.CallbackQuery):
    await bot.send_invoice(callback.from_user.id,
                           title="Конспект",
                           description="Плати за конспект",
                           provider_token=paytoken,
                           currency="rub",
                           prices=[LabeledPrice(label="конспект", amount=1000 * 100)],
                           payload="test-invoice-payload")
    await callback.message.edit_reply_markup(reply_markup=None)


@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(PayFilter())
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} \
{message.successful_payment.currency} прошел успешно!!!")
    if message.successful_payment.invoice_payload == "test-invoice-payload":
        await message.answer('здесь будет товар')