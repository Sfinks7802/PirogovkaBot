from aiogram import Router, F, types
from keyboards.get_contacts_kb import get_contacts_kb


router = Router()


@router.callback_query(F.data == 'contacts')
async def get_contacts(callback: types.CallbackQuery):
    await callback.message.edit_text('- Задать вопрос автору блога /сотрудничество @KseniyaKondrashkina' +f'\n'
                                  '- Любые вопросы по конспектам и материалам @pirogovka_helper \n'
                                     '- неофициальная ОФИЦИАЛЬНАЯ <a href="https://vk.com/kurs_202425">группа 1-курсников РНИМУ</a>', reply_markup=get_contacts_kb())
    await callback.answer()