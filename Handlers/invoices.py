from aiogram import Router, types, F
from aiogram.types import Message, LabeledPrice
from Bot import bot
import os
from all_contents import get_payed_content
from DataBase.db import update_contents
from Filters.InvoiceFilter import InvoiceFilter
from all_contents import get_file
from Handlers.links_generator import generate_link

router = Router()

lableprice = {
'with_yourself_gista_course': ['Курс по гисте', 1500],
'Oplata_letins': ['Гайд по учебе', 300],
'vskint_oplata': ['Вспомнить всё 4', 500],
'remember5_oplata': ['Вспомнить всё 5', 500],
'remember1_oplata': ['Вспомнить всё 1', 500],
'SerSod_conspect_pay': ['Конспект ССС', 300],
'Embriogenez_conspect_pay': ['Эмбриогенез', 300],
'remember1_1_pay': ['ВСПОМНИТЬ ВСЕ 1', 500],
'pishevar1_pay': ['ВЕБИНАР ПИЩЕВАРИТЕЛЬНАЯ 1', 500],
'klet_poverh_pay': ['Клеточная поверхность', 500],
'remember5_1_pay': ['Вспомнить всё 5', 500],
'epitely_pay': ['Эпителий веб', 500],
'web_nervy_pay': ['Нервы веб', 500],
'web_hrash_pay': ['Хрящевые веб', 500],
'web_kosty_pay': ['Костные веб', 500],
'remember6_pay': ['Вспомнить всё 6', 500],
'remember2_pay': ['Вспомнить всё 2', 700],
'remember3_pay': ['Вспомнить всё 3', 700],
'remember7_pay': ['Вспомнить всё 7', 700],
'org_chuv_pay': ['Органы чувств', 500],
'rotpol_pay': ['Введение + ротовая полость ', 200],
'okraski_conspect_pay': ['Методы окраски в гистологии', 200],
'nervnaya_sys_pay': ['Нервная система', 500],
'web_obsh_gist_pay': ['Общая гистология', 500],
'okraski_pay': ['Окраскии микроскоп', 500],
'anat_ekz_pay': ['Экзамен по анатомии', 1000],
'gist_ekz_oplata': ['Экзамен по гистологии', 4000],
'zadachi_pay': ['Задачи к экзамену', 300],
'cnsint_oplata': ['Интенсив по ЦНС', 1000],
'intensiv_cns_pay': ['Интенсив по ЦНС', 1000],
'with_courator_gista_course': ['Курс по гисте', 2500],
'anatint_oplata': ['Анатомия. Черепно-мозговые нервы.', 400],
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
            await message.answer('https://t.me/+_z_n5WYAgNJhOTBi')
            await bot.send_message(1924052002, text='Я сам гиста х1')
        elif flag == 'vskint_oplata':
            await message.answer('Отлично! Оплата прошла, скоро вам напишет помошник @pirogovka_helper')
            await bot.send_message(1924052002, text=f'Вспмнить всё х1, username пользователя: @{message.from_user.username}')
        elif flag == 'anatint_oplata':
            await message.answer('https://t.me/+mzccYh1g49JiMzAy')
            await bot.send_message(1924052002, text=f'Анатомия. Черепно-мозговые нервы х1, username пользователя: @{message.from_user.username}')
        elif flag == 'letins-invoice-payload':
            await message.answer('Здесь будет курс')
        elif flag == 'with_courator_gista_course':
            await message.answer('https://t.me/+_z_n5WYAgNJhOTBi \n'
                                 'общая группа по курсу гистологии \n'
                                 'https://t.me/+tGxG7_ZbWJ40MDcy \n'
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
        elif flag == 'web_hrash_pay':
            link = await generate_link(chat_id=-1002607919002)
            await message.answer(link)
            await bot.send_message(1924052002, text='Веб хрящевые х1')
        elif flag == 'web_kosty_pay':
            link = await generate_link(chat_id=-1002582782907)
            await message.answer(link)
            await bot.send_message(1924052002, text='Веб костные х1')
        elif flag == 'remember6_pay':
            link = await generate_link(chat_id=-1002611480243)
            await message.answer(link)
            await bot.send_message(1924052002, text='Вспомнить все 6 х1')
        elif flag == 'intensiv_cns_pay':
            link = await generate_link(chat_id=-1002616592114)
            await message.answer(link)
            await bot.send_message(1924052002, text='Интенсив ЦНС х1')
        elif flag == 'remember3_pay':
            link = await generate_link(chat_id=-1002619807577)
            await message.answer(link)
            await bot.send_message(1924052002, text='Вспомнить все 3 х1')
        elif flag == 'remember7_pay':
            link = await generate_link(chat_id=-1002682809666)
            await message.answer(link)
            await bot.send_message(1924052002, text='Вспомнить все 7 х1')
        elif flag == 'remember2_pay':
            link = await generate_link(chat_id=-1002504885575)
            await message.answer(link)
            await bot.send_message(1924052002, text='Вспомнить все 2 х1')
        elif flag == 'web_nervy_pay':
            link = await generate_link(chat_id=-1002547695736)
            await message.answer(link)
            await bot.send_message(1924052002, text='Веб нервы х1')
        elif flag == 'rotpol_pay':
            await message.answer_document(get_file('пищевар 1 .pdf'))
            await bot.send_message(1924052002, text='пищевар х1')
        elif flag == 'okraski_pay':
            await message.answer('https://t.me/+qxO4hMIIP104ZWEy')
            await bot.send_message(1924052002, text='окраски х1')
        elif flag == 'pishevar1_pay':
            await message.answer('https://t.me/+FzcBktlFDphmZGJi')
            await bot.send_message(1924052002, text='пищевар х1')
        elif flag == 'remember1_1_pay':
            await message.answer('https://t.me/+oTJTbtDtQPE1MTFi')
            await bot.send_message(1924052002, text='вспомнить все 1 х1')
        elif flag == 'epitely_pay':
            await message.answer('https://t.me/+tallwGXoEbQwN2My')
            await bot.send_message(1924052002, text='эпителий х1')
        elif flag == 'remember5_1_pay':
            await message.answer('https://t.me/+5o7BOx7MJZo5NmY6')
            await bot.send_message(1924052002, text='вспомнить всё 5 х1')
        elif flag == 'org_chuv_pay':
            await message.answer('https://t.me/+EyPRfViPmSc1N2Iy')
            await bot.send_message(1924052002, text='органы чувств х1')
        elif flag == 'okraski_conspect_pay':
            await message.answer_document(get_file('Методы окраски .pdf'))
            await bot.send_message(1924052002, text='окраски конспект х1')
        elif flag == 'nervnaya_sys_pay':
            await message.answer('https://t.me/+OFH5J3bVvvJkZTVi')
            await bot.send_message(1924052002, text='нервная система ЦНС х1')
        elif flag == 'klet_poverh_pay':
            await message.answer('https://t.me/+g6g7QU21w-dmNjIy')
            await bot.send_message(1924052002, text='клеточная поверхность х1')
        elif flag == 'web_obsh_gist_pay':
            await message.answer('https://t.me/+QOZlfbaiK9BmYjky')
            await bot.send_message(1924052002, text='общая гистология х1')
        elif flag == 'anat_ekz_pay':
            await message.answer('https://t.me/+coYCZWjbNO9lYzFi')
            await bot.send_message(1924052002, text='Анатомия экзамен х1')
        elif flag == 'zadachi_pay':
            await message.answer_document(get_file('Задачи к экзамену.pdf'))
            await bot.send_message(1924052002, text='Задачи к экзамену х1')
        elif flag == 'remember5_oplata':
            await message.answer('https://t.me/+RWQZjfbcmc03MjYy')
            await bot.send_message(1924052002, text='Вспомнить всё 5 х1')
        elif flag == 'remember1_oplata':
            await message.answer('https://t.me/+lnaoEUIYZVhlY2Uy')
            await bot.send_message(1924052002, text='Вспомнить всё 1 х1')
        elif flag == 'gist_ekz_oplata':
            await message.answer('https://t.me/+by534wVm_XcwMGYy')
            await bot.send_message(1924052002, text='Гиста экзамен х1')
        elif flag == 'SerSod_conspect_pay':
            await message.answer_document(get_file('Конспект_ССС.pdf'))
            await bot.send_message(1924052002, text='Конспект ССС х1')
        elif flag == 'Embriogenez_conspect_pay':
            await message.answer_document(get_file('Лекция_2_эмбриогенез.pdf'))
            await bot.send_message(1924052002, text='Лекция_2_эмбриогенез х1')
    except Exception:
        await message.answer('Упс! Кажется произошла какая-то непрвиденная ошибка( \n'
                             'напишите @pirogovka_helper\n'
                             'отчет уже отправлен поддержке')
        await bot.send_message(1924052002, text=f'Опять ошибка( техническое имя товара: {flag}, username пользователя: @{message.from_user.username}')
