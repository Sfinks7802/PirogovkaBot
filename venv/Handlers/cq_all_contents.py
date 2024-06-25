from aiogram import types, F, Router
from keyboards.all_contents_kb import (get_kb_all_free, get_kb_BiologiyaWebs, get_kb_Colok1Web, get_kb_Colok3Web,
    get_kb_GistologiyaWebs, get_kb_Colok2Web, get_kb_all_webs, get_kb_all_conspects, get_kb_AnatomiyaWebs, get_kb_all_contents,
                                       get_kb_Himiya, get_kb_Myshcy, get_kb_Pishevar, get_kb_Colok1, get_kb_Colok2, get_kb_Colok3,
                                       get_kb_Anatomiya, get_kb_CNS, get_kb_Gistologiya, get_kb_Biologiya, get_kb_Osteologiya, get_kb_Pol_conspect,
                                       get_kb_Dyh_i_moch, get_kb_Sustavy)


router = Router()


@router.callback_query(F.data == 'all_contents')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.answer('Выберите категорию', reply_markup=get_kb_all_contents())
    await callback.answer()


@router.callback_query(F.data == 'all_free')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_free())
    await callback.answer()


@router.callback_query(F.data == 'all_conspects')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_conspects())
    await callback.answer()


@router.callback_query(F.data == 'all_webs')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_webs())
    await callback.answer()


@router.callback_query(F.data == 'Anatomiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Anatomiya())
    await callback.answer()


@router.callback_query(F.data == 'Gistologiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Gistologiya())
    await callback.answer()


@router.callback_query(F.data == 'Osteologiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Osteologiya())
    await callback.answer()


@router.callback_query(F.data == 'CNS')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_CNS())
    await callback.answer()


@router.callback_query(F.data == 'Myshcy')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Myshcy())
    await callback.answer()


@router.callback_query(F.data == 'Pishevar')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Pishevar())
    await callback.answer()


@router.callback_query(F.data == 'Dyh_i_moch')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Dyh_i_moch())
    await callback.answer()


@router.callback_query(F.data == 'Sustavy')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Sustavy())
    await callback.answer()


@router.callback_query(F.data == 'Back_to_Anatomiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Anatomiya())
    await callback.answer()


@router.callback_query(F.data == 'Back_to_all_conspects')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_conspects())
    await callback.answer()


@router.callback_query(F.data == 'Back_to_all_contents')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_contents())
    await callback.answer()


@router.callback_query(F.data == 'Colok1')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok1())
    await callback.answer()


@router.callback_query(F.data == 'Colok2')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok2())
    await callback.answer()


@router.callback_query(F.data == 'Colok3')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok3())
    await callback.answer()


@router.callback_query(F.data == 'Back_to_Gistologiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Gistologiya())
    await callback.answer()


@router.callback_query(F.data == 'Biologiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Biologiya())
    await callback.answer()


@router.callback_query(F.data == 'Himiya')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Himiya())
    await callback.answer()


@router.callback_query(F.data == 'Pol_conspect')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Pol_conspect())
    await callback.answer()


@router.callback_query(F.data == 'Colok1Web')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok1Web())
    await callback.answer()


@router.callback_query(F.data == 'Colok2Web')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok2Web())
    await callback.answer()


@router.callback_query(F.data == 'Colok3Web')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Colok3Web())
    await callback.answer()


@router.callback_query(F.data == 'AnatomiyaWebs')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_AnatomiyaWebs())
    await callback.answer()


@router.callback_query(F.data == 'GistologiyaWebs')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_GistologiyaWebs())
    await callback.answer()


@router.callback_query(F.data == 'BiologiyaWebs')
async def all_contents( callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_BiologiyaWebs())
    await callback.answer()

@router.callback_query(F.data == 'Back_to_Dyh_i_moch')
async def all_contents(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_Dyh_i_moch())
    await callback.answer()


@router.callback_query(F.data == 'Back_to_all_webs')
async def all_contents(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_kb_all_webs())
    await callback.answer()