from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ChatMemberLeft
from Bot import bot
from keyboards.menu_kb import get_kb_for_sub
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub_bibla
from DataBase.db import new_user, find_user
from texts.all_texts import gista_course_txt, letniy_intensiv_2_text, letniy_intensiv_text, cnsint_txt, not_sub_txt
from Handlers.gista_course import get_kb_for_gista_course
from Handlers.cq_letniy_intensiv import get_kb_leto
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.message(CommandStart(deep_link=True, magic=F.args == 'gist_course'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    await message.answer(gista_course_txt, reply_markup=get_kb_for_gista_course())


@router.message(CommandStart(deep_link=True, magic=F.args == 'cnsint'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (1000р)", callback_data='!cnsint_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(cnsint_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'learn_gide'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    await message.answer(letniy_intensiv_text)
    await message.answer(text=letniy_intensiv_2_text, reply_markup=get_kb_leto())


@router.callback_query(F.data == 'sub_done')
async def check_sub(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='-1001841308905', user_id=callback.from_user.id)
    if not isinstance(user_channel_status, ChatMemberLeft):
        await callback.message.answer('Спасибо, теперь бот будет работать!')
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()

@router.callback_query(F.data == 'sub_done_bibla')
async def check_sub(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='-1002209887331', user_id=callback.from_user.id)
    user_channel_status_2 = await bot.get_chat_member(chat_id='-1001841308905', user_id=callback.from_user.id)
    if not isinstance(user_channel_status, ChatMemberLeft) and not isinstance(user_channel_status_2, ChatMemberLeft):
        await callback.message.answer('Спасибо,'
                                      ' вы можете воспользовать библиотекой студента')
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.answer()
    else:
        await callback.message.edit_text(not_sub_txt, reply_markup=get_keyboard_for_not_sub_bibla())


@router.message(Command('start'))
async def cmd_start(message: Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    await message.answer('Добро пожаловать!',reply_markup=get_kb_for_sub())

