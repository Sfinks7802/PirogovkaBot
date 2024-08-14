from aiogram import Router, types, F
from aiogram.types import Message, LabeledPrice
from Bot import bot
import os
from all_contents import get_payed_content
from DataBase.db import update_contents
from Filters.InvoiceFilter import InvoiceFilter

router = Router()

lableprice = {
'with_yourself_gista_course': ['Курс по гисте', 1500],
'Oplata_letins': ['Гайд по учебе', 300],
'with_courator_gista_course': ['Курс по гисте', 2500],
'with_auther_gista_course': ['Курс по гисте', 4500]
}


@router.callback_query(InvoiceFilter())
async def pay_money(callback: types.CallbackQuery):
    await bot.send_invoice(callback.from_user.id,
                           title="Виртуальный товар",
                           description="Оплата виртуального товара",
                           provider_token=os.environ.get('paytoken'),
                           currency="rub",
                           prices=[LabeledPrice(label=lableprice[callback.data[1::]][0], amount=lableprice[callback.data[1::]][1] * 100)],
                           payload=callback.data[1::],
                           protect_content=True)
    await callback.answer()


@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# @router.message(PayFilter())
# async def successful_payment(message: types.Message):
#     update_contents(message.from_user.id, message.successful_payment.invoice_payload)
#     await message.answer_document(get_payed_content(message.successful_payment.invoice_payload))


@router.message(F.successful_payment)
async def successful_payment(message: types.Message):
    flag = message.successful_payment.invoice_payload
    if flag == 'with_yourself_gista_course':
        await message.answer('https://t.me/+eNrEtEmJ3jc4OTky')
    elif flag == 'letins-invoice-payload':
        await message.answer('Здесь будет курс')
    elif flag == 'with_courator_gista_course':
        await message.answer('https://t.me/+eNrEtEmJ3jc4OTky \n'
                             'общая группа по курсу гистологии \n'
                             'https://t.me/+VAoNn_scisQ0ZWUy \n'
                             'группа с куратором')
    elif flag == 'with_auther_gista_course':
        await message.answer('https://t.me/+eNrEtEmJ3jc4OTky \n'
                             'общая группа по курсу гистологии \n'
                             'https://t.me/+VAoNn_scisQ0ZWUy \n'
                             'группа с автором курса')
