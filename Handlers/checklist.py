from aiogram import Router, F, types
from texts.all_texts import checklist_txt
from all_contents import get_file
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.callback_query(F.data == 'checklist')
async def get_contacts(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
    await callback.message.edit_text(checklist_txt, reply_markup=builder.as_markup())
    await callback.message.answer_document(get_file('чек_лист_Версия_студенты_университета.pdf'))
    await callback.answer()