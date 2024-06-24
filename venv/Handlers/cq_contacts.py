from aiogram import Router, F, types
from keyboards.get_contacts_kb import get_contacts_kb


router = Router()


@router.callback_query(F.data == 'contacts')
async def get_contacts(callback: types.CallbackQuery):
    await callback.message.answer('- Задать вопрос автору блога /сотрудничество @KseniyaKondrashkina' +f'\n'
                                  '- Любые вопросы по конспектам и материалам @pirogovka_helper', reply_markup=get_contacts_kb())
    await callback.answer()