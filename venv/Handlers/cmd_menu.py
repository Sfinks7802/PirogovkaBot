from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.menu_kb import get_kb_for_sub, get_kb_Pirogovka_matirials


router = Router()


@router.message(Command('menu'))
async def get_menu(message: types.Message):
    await message.answer('Выберите категорию', reply_markup=get_kb_for_sub())


@router.callback_query(F.data == 'Pirogovka_matirials')
async def get_Pirogovka_matirials(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Pirogovka_matirials())