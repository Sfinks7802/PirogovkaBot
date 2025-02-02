from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import (okraski_conspect_txt)
from aiogram import Router, types, F
from all_contents import get_file



router = Router()



def new_cq(f_txt: str, cq_txt: str, pay_txt: str, msg_txt):
    @router.callback_query(F.data == f_txt)
    async def get_contacts(callback: types.CallbackQuery):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text=cq_txt, callback_data=pay_txt))
        builder.row(types.InlineKeyboardButton(text="Назад", callback_data='menu'))
        await callback.message.answer(text=msg_txt, reply_markup=builder.as_markup(), parse_mode='HTML')
        await callback.answer()


# def new_file_ans(f_txt: str, cq_txt: str, pay_txt: str, msg_txt):
#     @router.callback_query(F.data == f_txt)
#     async def get_contacts(callback: types.CallbackQuery):
#         builder = InlineKeyboardBuilder()
#         builder.row(types.InlineKeyboardButton(text="Назад", callback_data='Pirogovka_matirials'))
#         await callback.message.edit_text(checklist_txt, reply_markup=builder.as_markup())
#         await callback.message.answer_document(get_file('чек_лист_Версия_студенты_университета.pdf'))
#         await callback.answer()

new_cq('okraski_conspect','Купить (200р)', '!okraski_conspect_pay', okraski_conspect_txt)