from aiogram import types


def get_kb_for_intro():
    buttons = [[types.InlineKeyboardButton(text="📖 Что внутри гайда", callback_data="guide_v2_whats_inside")],
               [types.InlineKeyboardButton(text="❤️ Кому подойдёт", callback_data="guide_v2_target_audience")],
               [types.InlineKeyboardButton(text="💰 Купить сейчас", callback_data="guide_v2_buy_now")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_fasttrack():
    buttons = [[types.InlineKeyboardButton(text="💰 Купить (1690₽)", callback_data="guide_v2_buy_now")],
               [types.InlineKeyboardButton(text="📖 Посмотреть пример", callback_data="guide_v2_example_page")],
               [types.InlineKeyboardButton(text="⬅️ Хочу освежить, что внутри", callback_data="guide_v2_whats_inside")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_whats_inside():
    buttons = [[types.InlineKeyboardButton(text="🔍 Подробнее по главам", callback_data="guide_v2_contents")],
               [types.InlineKeyboardButton(text="🎁 Хочу пример страницы", callback_data="guide_v2_example_page")],
               [types.InlineKeyboardButton(text="💰 Купить со скидкой", callback_data="guide_v2_buy_now")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_contents():
    buttons = [[types.InlineKeyboardButton(text="❤️ Кому пригодится", callback_data="guide_v2_target_audience")],
               [types.InlineKeyboardButton(text="💰 Хочу купить", callback_data="guide_v2_buy_now")],
               [types.InlineKeyboardButton(text="⬅️ Назад", callback_data="guide_v2_whats_inside")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_example_page():
    buttons = [[types.InlineKeyboardButton(text="💰 Купить гайд", callback_data="guide_v2_buy_now")],
               [types.InlineKeyboardButton(text="📎 Назад в меню", callback_data="guide_v2_whats_inside")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_target_audience():
    buttons = [[types.InlineKeyboardButton(text="💡 Посмотреть отзывы", callback_data="guide_v2_reviews")],
               [types.InlineKeyboardButton(text="💰 Купить (1690₽)", callback_data="guide_v2_buy_now")],
               [types.InlineKeyboardButton(text="💡 Куда уходит энергия?", callback_data="guide_v2_questionnaire")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_reviews():
    buttons = [[types.InlineKeyboardButton(text="💰 Хочу гайд", callback_data="guide_v2_buy_now")],
               [types.InlineKeyboardButton(text="📘 Пример страниц", callback_data="guide_v2_example_page")],
               [types.InlineKeyboardButton(text="⬅️ Назад", callback_data="guide_v2_target_audience")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_questionnaire():
    buttons = [[types.InlineKeyboardButton(text="🕓 Не успеваю по времени", callback_data="guide_v2_questionnaire_answer_time")],
               [types.InlineKeyboardButton(text="🧩 Не запоминаю надолго", callback_data="guide_v2_questionnaire_answer_memory")],
               [types.InlineKeyboardButton(text="💤 Нет мотивации", callback_data="guide_v2_questionnaire_answer_motivation")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_questionnaire_response():
    buttons = [[types.InlineKeyboardButton(text="📘 Пример страниц", callback_data="guide_v2_example_page")],
               [types.InlineKeyboardButton(text="💰 Хочу гайд", callback_data="guide_v2_buy_now")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_for_oferta_agree():
    buttons = [[types.InlineKeyboardButton(text="Согласен", callback_data="!time_guide_pay_50")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard