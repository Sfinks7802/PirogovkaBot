from calendar import c
from aiogram import types, F, Router
from keyboards.guide_v2_kb import get_kb_for_intro, get_kb_for_fasttrack, get_kb_for_whats_inside, get_kb_for_contents, get_kb_for_example_page, get_kb_for_target_audience, get_kb_for_reviews, get_kb_for_questionnaire, get_kb_for_questionnaire_response, get_kb_for_oferta_agree
from texts.all_texts import guide_v2_intro_txt, guide_v2_fasttrack_txt, guide_v2_whats_inside_txt, guide_v2_contents_txt, guide_v2_example_page_txt, guide_v2_target_audience_txt, guide_v2_reviews_txt, guide_v2_questionnaire_txt
from all_contents import get_file

router = Router()


@router.callback_query(F.data == 'guide_v2_intro')
async def get_intro( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_intro_txt, reply_markup=get_kb_for_intro())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_fasttrack')
async def get_fasttrack( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_fasttrack_txt, reply_markup=get_kb_for_fasttrack())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_whats_inside')
async def get_whats_inside( callback: types.CallbackQuery):
    if (callback.message.content_type == types.ContentType.TEXT):
        await callback.message.edit_text(guide_v2_whats_inside_txt, reply_markup=get_kb_for_whats_inside())
        await callback.answer()
    elif (callback.message.content_type == types.ContentType.PHOTO):
        await callback.message.delete()
        await callback.message.answer(guide_v2_whats_inside_txt, reply_markup=get_kb_for_whats_inside())

@router.callback_query(F.data == 'guide_v2_contents')
async def get_contents( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_contents_txt, reply_markup=get_kb_for_contents())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_example_page')
async def get_example_page( callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo=get_file('example_page.jpg', subdir='guide_v2'), caption=guide_v2_example_page_txt, reply_markup=get_kb_for_example_page(), parse_mode='HTML')
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_target_audience')
async def get_target_audience( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_target_audience_txt, reply_markup=get_kb_for_target_audience())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_reviews')
async def get_reviews( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_reviews_txt, reply_markup=get_kb_for_reviews(), parse_mode='MarkdownV2')
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_questionnaire')
async def get_guide_v2_questionnaire( callback: types.CallbackQuery):
    await callback.message.edit_text(guide_v2_questionnaire_txt, reply_markup=get_kb_for_questionnaire())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_questionnaire_answer_time')
async def get_guide_v2_questionnaire_answer_time( callback: types.CallbackQuery):
    await callback.message.edit_text("Тогда тебе подойдёт глава  про планирование без выгорания. Там есть шаблон недели и схема повторений 🕓", reply_markup=get_kb_for_questionnaire_response())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_questionnaire_answer_memory')
async def get_guide_v2_questionnaire_answer_memory( callback: types.CallbackQuery):
    await callback.message.edit_text("Значит, тебе точно будет полезна глава  “Активное воспоминание”. Покажу, как запоминать надолго 💡", reply_markup=get_kb_for_questionnaire_response())
    await callback.answer()

@router.callback_query(F.data == 'guide_v2_questionnaire_answer_motivation')
async def get_guide_v2_questionnaire_answer_motivation( callback: types.CallbackQuery):
    await callback.message.edit_text("Понимаю! Именно для этого есть глава “Самодисциплина без насилия над собой”. ❤️", reply_markup=get_kb_for_questionnaire_response())
    await callback.answer()


@router.callback_query(F.data == 'guide_v2_buy_now')
async def get_guide_v2_oferta( callback: types.CallbackQuery):
    await callback.message.answer("Продолжая покупку, вы соглашаетесь с офертой", reply_markup=get_kb_for_oferta_agree())
    await callback.answer()