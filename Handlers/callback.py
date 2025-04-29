from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts.all_texts import (okraski_conspect_txt, rotpol_txt, klet_poverh_txt, org_chuv_txt, remember5_1_txt, epiteliy_txt,
                             pishevar1_txt, remember1_1_txt, web_obsh_gist_txt, web_hrash_txt, web_kosty_txt, remember6_txt,
                             remember2_txt, web_nervy_txt)
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
new_cq('rotpol', 'Купить (200р)', '!rotpol_pay', rotpol_txt)
new_cq('klet_poverh', 'Купить (500р)', '!klet_poverh_pay', klet_poverh_txt)
new_cq('org_chuv', 'Купить (500)', '!org_chuv_pay', org_chuv_txt)
new_cq('remember5_1', 'Купить (500)', '!remember5_1_pay', remember5_1_txt)
new_cq('epitely', 'Купить (500р)', '!epitely_pay', epiteliy_txt)
new_cq('remember1_1', 'Купить (500р)', '!remember1_1_pay', remember1_1_txt)
new_cq('pishevar1', 'Купить (500р)', '!pishevar1_pay', pishevar1_txt)
new_cq('web_obsh_gist', 'Купить (500р)', '!web_obsh_gist_pay', web_obsh_gist_txt)
new_cq('web_hrash', 'Купить (500р)', '!web_hrash_pay', web_hrash_txt)
new_cq('web_kosty', 'Купить (500р)', '!web_kosty_pay', web_kosty_txt)
new_cq('remember6', 'Купить (500р)', '!remember6_pay', remember6_txt)
new_cq('remember2', 'Купить (700р)', '!remember2_pay', remember2_txt)
new_cq('web_nervy', 'Купить (500р)', '!web_nervy_pay', web_nervy_txt)