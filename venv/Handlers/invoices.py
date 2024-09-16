from aiogram import Router, types, F
from aiogram.types import Message, LabeledPrice
from Bot import bot
import os
from all_contents import get_payed_content
from DataBase.db import update_contents
from Filters.InvoiceFilter import InvoiceFilter
from all_contents import get_file

router = Router()

lableprice = {
'with_yourself_gista_course': ['Курс по гисте', 1500],
'Oplata_letins': ['Гайд по учебе', 300],
'SerSod_conspect_pay': ['Конспект ССС', 300],
'cnsint_oplata': ['Интенсив по ЦНС', 1000],
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
    try:
        if flag == 'with_yourself_gista_course':
            await message.answer('https://t.me/+eNrEtEmJ3jc4OTky')
            await bot.send_message(1924052002, text='Я сам гиста х1')
        elif flag == 'letins-invoice-payload':
            await message.answer('Здесь будет курс')
        elif flag == 'with_courator_gista_course':
            await message.answer('https://t.me/+eNrEtEmJ3jc4OTky \n'
                                 'общая группа по курсу гистологии \n'
                                 'https://t.me/+VAoNn_scisQ0ZWUy \n'
                                 'группа с куратором')
            await bot.send_message(1924052002, text='Куратор гиста х1')
        elif flag == 'with_auther_gista_course':
            await message.answer('https://t.me/+eNrEtEmJ3jc4OTky \n'
                                 'общая группа по курсу гистологии \n'
                                 'https://t.me/+VAoNn_scisQ0ZWUy \n'
                                 'группа с автором курса')
            await bot.send_message(1924052002, text='Автор курса гиста х1')
        elif flag == 'cnsint_oplata':
            await message.answer('https://t.me/+qvReZgCkdpdiZTgy')
            await bot.send_message(1924052002, text='Интенсив ЦНС х1')
        elif flag == 'SerSod_conspect_pay':
            await message.answer_document(get_file('Конспект_ССС.pdf'))
            await bot.send_message(1924052002, text='Конспект ССС х1')
    except Exception:
        await message.answer('Упс! Кажется произошла какая-то непрвиденная ошибка( \n'
                             'напишите @pirogovka_helper\n'
                             'отчет уже отправлен поддержке')
        await bot.send_message(1924052002, text=f'Опять ошибка( техническое имя товара: {flag}, username пользователя: @{message.from_user.username}')
