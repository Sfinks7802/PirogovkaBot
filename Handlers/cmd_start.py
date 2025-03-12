from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ChatMemberLeft
from Bot import bot
from keyboards.menu_kb import get_kb_for_sub
from keyboards.start_not_sub_kb import get_keyboard_for_not_sub_bibla
from DataBase.db import new_user, find_user
from texts.all_texts import (gista_course_txt, letniy_intensiv_2_text, letniy_intensiv_text, cnsint_txt, not_sub_txt, bibla_text,
                             sersod_txt, anatint_txt, embriogenez_txt, remember5_txt, remember1_txt, gista_ekz_txt, anat_ekz_txt,
                             zadachi_txt, okraski_txt, nervnaya_sys_txt, okraski_conspect_txt, rotpol_txt, klet_poverh_txt,
                             org_chuv_txt, remember5_1_txt, epiteliy_txt, pishevar1_txt, remember1_1_txt)
from Handlers.gista_course import get_kb_for_gista_course
from Handlers.cq_letniy_intensiv import get_kb_leto
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Handlers.bibla import get_kb_bibla
from all_contents import get_file


router = Router()


def new_startlink(link_txt: str, cq_txt: str, pay_txt: str, msg_txt):
    @router.message(CommandStart(deep_link=True, magic=F.args == link_txt))
    async def get_guist_course(message: types.Message):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text=cq_txt, callback_data=pay_txt))
        builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
        await message.answer(msg_txt, reply_markup=builder.as_markup())


new_startlink('okraski_conspect','Купить (200р)', '!okraski_conspect_pay', okraski_conspect_txt)
new_startlink('rotpol', 'Купить (200р)', '!rotpol_pay', rotpol_txt)
new_startlink('klet_poverh', 'Купить (500р)', '!klet_poverh_pay', klet_poverh_txt)
new_startlink('org_chuv', 'Купить (500)', '!org_chuv_pay', org_chuv_txt)
new_startlink('remember5_1', 'Купить (500)', '!remember5_1_pay', remember5_1_txt)
new_startlink('epitely', 'Купить (500р)', '!epitely_pay', epiteliy_txt)
new_startlink('remember1_1', 'Купить (500р)', '!remember1_1_pay', remember1_1_txt)
new_startlink('pishevar1', 'Купить (500р)', '!pishevar1_pay', pishevar1_txt)


@router.message(CommandStart(deep_link=True, magic=F.args == 'gist_course'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    await message.answer(gista_course_txt, reply_markup=get_kb_for_gista_course())


@router.message(CommandStart(deep_link=True, magic=F.args == 'anat_int'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!remember5_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(anatint_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'zadachi'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!zadachi_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(zadachi_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'okraski'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!okraski_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(okraski_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'nervnaya_sys'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!nervnaya_sys_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(nervnaya_sys_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'gist_ekz'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (4000р)", callback_data='!gist_ekz_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(gista_ekz_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'remember5'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!remember5_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(remember5_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'remember1'))
async def get_guist_course(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (500р)", callback_data='!remember1_oplata'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await message.answer(remember1_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'SerSod'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!SerSod_conspect_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await message.answer_photo(photo=get_file('SerSod_photo.jpg'), caption=sersod_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'anat_ekz'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (1000р)", callback_data='!anat_ekz_pay'))
    builder.row(types.InlineKeyboardButton(text="Вопросы для чата", callback_data='anat_ekz_shpora'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await message.answer_photo(photo=get_file('anat_ekz.jpg'), caption=anat_ekz_txt, reply_markup=builder.as_markup())


@router.message(CommandStart(deep_link=True, magic=F.args == 'Embriogenez'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!Embriogenez_conspect_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await message.answer_photo(photo=get_file('embriogenez.jpg'), caption=embriogenez_txt, reply_markup=builder.as_markup(), parse_mode='HTML')


@router.message(CommandStart(deep_link=True, magic=F.args == 'bibla'))
async def get_guist_course(message: types.Message):
    if type(find_user(message.from_user.id)) == None:
        new_user(message.from_user.id)
    await message.answer(bibla_text, reply_markup=get_kb_bibla())


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

