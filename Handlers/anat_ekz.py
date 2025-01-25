from aiogram import Router, F, types
from texts.all_texts import anat_ekz_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder
from all_contents import get_file


router = Router()


@router.callback_query(F.data == 'anat_ekz')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (1000р)", callback_data='!anat_ekz_pay'))
    builder.row(types.InlineKeyboardButton(text="Вопросы для чата", callback_data='anat_ekz_shpora'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer_photo(photo=get_file('anat_ekz.jpg'), caption=anat_ekz_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
    await callback.answer()


@router.callback_query(F.data == 'anat_ekz_shpora')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (1000р)", callback_data='!anat_ekz_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='anat_ekz'))
    await callback.message.answer_photo(photo=get_file('anat_ekz_2.jpg'), reply_markup=builder.as_markup(), parse_mode='HTML')
    await callback.answer()