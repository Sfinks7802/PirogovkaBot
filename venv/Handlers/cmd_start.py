from aiogram import Router, types, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message, ChatMemberLeft, LabeledPrice
from PrivatInfo import bot, paytoken
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


class PayFilter(BaseFilter):
    async def __call__(self, message: types.Message):
        if message.successful_payment:
            return True
        else:
            return False



def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Оф. канал Telegram", url="https://t.me/pirogovka_now")],
        [types.InlineKeyboardButton(text="Я подписался", callback_data="sub_done")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard



@router.callback_query(F.data == 'sub_done')
async def check_sub(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=callback.from_user.id)
    if not isinstance(user_channel_status, ChatMemberLeft):
        await callback.message.answer('Спасибо')
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()

@router.callback_query(F.data == 'pay_your_money')
async def pay_money(callback: types.CallbackQuery):
    await bot.send_invoice(callback.from_user.id,
                           title="Конспект",
                           description="Плати за конспект",
                           provider_token=paytoken,
                           currency="rub",
                           prices=[LabeledPrice(label="конспект", amount=1000 * 100)],
                           start_parameter="deposit",
                           payload="test-invoice-payload")
    await callback.message.edit_reply_markup(reply_markup=None)


@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(PayFilter())
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")

@router.message(Command('start'))
async def cmd_start(message: Message):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=message.from_user.id)
    if isinstance(user_channel_status, ChatMemberLeft):
        await message.answer('Для использования бота подпишитесь на канал', reply_markup=get_keyboard())
    else:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="Отдать свои деньги", callback_data="pay_your_money"))
        await message.answer('Плати',reply_markup=builder.as_markup())

