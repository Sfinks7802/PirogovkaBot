from aiogram import Router, F, types
from texts.all_texts import sersod_txt, embriogenez_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder
from all_contents import get_file


router = Router()


@router.callback_query(F.data == 'SerSod_conspect')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!SerSod_conspect_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer_photo(photo=get_file('SerSod_photo.jpg'), caption=sersod_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
    # await callback.message.edit_media(media=get_file('SerSod_photo'), reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == 'Embriogenez_conspect')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Купить (300р)", callback_data='!Embriogenez_conspect_pay'))
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
    await callback.message.answer_photo(photo=get_file('embriogenez.jpg'), caption=embriogenez_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
    await callback.answer()