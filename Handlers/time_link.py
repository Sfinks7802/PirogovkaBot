from aiogram import Router, F, types
from texts.all_texts import time_guide_txt, guide_who_txt, guide_in_txt, guide_chapters_txt, readFile, low_price_txt
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'time_guide')
async def get_guide(callback: types.CallbackQuery):
    # await callback.message.answer('qwety')
    counter = int(readFile('counter.txt'))
    if counter < 50:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="Купить (845р)", callback_data='!time_guide_pay'))
        builder.row(types.InlineKeyboardButton(text="О гайде", callback_data='time_guide'))
        builder.row(types.InlineKeyboardButton(text="СКИДКА", callback_data='low_price'))
        builder.row(types.InlineKeyboardButton(text="Что внутри?", callback_data='guide_in'))
        builder.row(types.InlineKeyboardButton(text="Подробнее по главам", callback_data='guide_chapters'))
        builder.row(types.InlineKeyboardButton(text="Кому пригодится этот гайд?", callback_data='guide_who'))
        builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
        await callback.message.edit_text(time_guide_txt, reply_markup=builder.as_markup())
        await callback.answer()
    else:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="Купить (845р)", callback_data='!time_guide_pay'))
        builder.row(types.InlineKeyboardButton(text="О гайде", callback_data='time_guide'))
        builder.row(types.InlineKeyboardButton(text="Что внутри?", callback_data='guide_in'))
        builder.row(types.InlineKeyboardButton(text="Подробнее по главам", callback_data='guide_chapters'))
        builder.row(types.InlineKeyboardButton(text="Кому пригодится этот гайд?", callback_data='guide_who'))
        builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
        await callback.message.edit_text(time_guide_txt, reply_markup=builder.as_markup())
        await callback.answer()


@router.callback_query(F.data == 'guide_in')
async def get_guide(callback: types.CallbackQuery):
    await callback.message.edit_text(guide_in_txt, reply_markup=callback.message.reply_markup)
    await callback.answer()


@router.callback_query(F.data == 'guide_chapters')
async def get_guide(callback: types.CallbackQuery):
    await callback.message.edit_text(guide_chapters_txt, reply_markup=callback.message.reply_markup)
    await callback.answer()


@router.callback_query(F.data == 'guide_who')
async def get_guide(callback: types.CallbackQuery):
    await callback.message.edit_text(guide_who_txt, reply_markup=callback.message.reply_markup)
    await callback.answer()


@router.callback_query(F.data == 'low_price')
async def get_guide(callback: types.CallbackQuery):
    await callback.message.edit_text(low_price_txt, reply_markup=callback.message.reply_markup)
    await callback.answer()