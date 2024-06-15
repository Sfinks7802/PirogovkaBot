from aiogram import Router, F, types


router = Router()


@router.callback_query(F.data == 'gist_course')
async def get_guist_course(callback: types.CallbackQuery):
    await callback.message.answer('В разработке...')
    await callback.answer()