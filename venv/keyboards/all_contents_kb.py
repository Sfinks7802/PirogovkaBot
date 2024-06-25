from aiogram import types


def get_kb_all_contents():
    buttons = [[types.InlineKeyboardButton(text="Бесплатные материалы", callback_data="all_free")],
               [types.InlineKeyboardButton(text="Конспекты", callback_data="all_conspects")],
               [types.InlineKeyboardButton(text="Вебинары", callback_data="all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_all_conspects():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", callback_data="Anatomiya")],
               [types.InlineKeyboardButton(text="Биология", callback_data="Biologiya")],
               [types.InlineKeyboardButton(text="Гистология", callback_data="Gistologiya")],
               [types.InlineKeyboardButton(text="Химия", callback_data="Himiya")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_contents")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Anatomiya():
    buttons = [[types.InlineKeyboardButton(text="Дых. и мочепол. системы", callback_data="Dyh_i_moch")],
               [types.InlineKeyboardButton(text="Мышцы", callback_data="Myshcy")],
               [types.InlineKeyboardButton(text="Остеология", callback_data="Osteologiya")],
               [types.InlineKeyboardButton(text="Пищевар. система", callback_data="Pishevar")],
               [types.InlineKeyboardButton(text="Суставы", callback_data="Sustavy")],
               [types.InlineKeyboardButton(text="ЦНС", callback_data="CNS")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_conspects")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Biologiya():
    buttons = [[types.InlineKeyboardButton(text="Билеты 1-20 био.", callback_data="Bilety_1-20")],
               [types.InlineKeyboardButton(text="Билеты 21-40 био.", callback_data="Bilety_21-40")],
               [types.InlineKeyboardButton(text="Билеты 41-60 био.", callback_data="Bilety_41-60")],
               [types.InlineKeyboardButton(text="Задачи био.", callback_data="Zadachi")],
               [types.InlineKeyboardButton(text="Лабораторная био.", callback_data="Laboratornaya")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_conspects")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Gistologiya():
    buttons = [[types.InlineKeyboardButton(text="Колок гист 1-й", callback_data="Colok1")],
               [types.InlineKeyboardButton(text="Колок гист 2-й", callback_data="Colok2")],
               [types.InlineKeyboardButton(text="Колок гист 3-й", callback_data="Colok3")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_conspects")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Himiya():
    buttons = [[types.InlineKeyboardButton(text="Карточки хим. 4 колок", callback_data="Colok4")],
               [types.InlineKeyboardButton(text="Карточки хим. 5 колок", callback_data="Colok5")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_conspects")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Dyh_i_moch():
    buttons = [[types.InlineKeyboardButton(text="Дых. и мочепол. колок", callback_data="Dyh_i_moch_colok")],
               [types.InlineKeyboardButton(text="Дыхательная сис. конспект", callback_data="Dyh_conspect")],
               [types.InlineKeyboardButton(text="Мочевыделительная сис. конспект", callback_data="Moch_conspect")],
               [types.InlineKeyboardButton(text="Половая конспект", callback_data="Pol_conspect")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Pol_conspect():
    buttons = [[types.InlineKeyboardButton(text="Мужская пол. сис.", callback_data="Pol_muj")],
               [types.InlineKeyboardButton(text="Женская пол. сис.", callback_data="Pol_jen")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Dyh_i_moch")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Myshcy():
    buttons = [[types.InlineKeyboardButton(text="Диафрагма мышцы", callback_data="Diafragma")],
               [types.InlineKeyboardButton(text="Грудь мышцы", callback_data="Grud'")],
               [types.InlineKeyboardButton(text="Живот мышцы", callback_data="Jivot")],
               [types.InlineKeyboardButton(text="Спина мышцы", callback_data="Spina")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Osteologiya():
    buttons = [[types.InlineKeyboardButton(text="Конечности", callback_data="Konechnosti")],
               [types.InlineKeyboardButton(text="Череп", callback_data="Cherep")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Pishevar():
    buttons = [[types.InlineKeyboardButton(text="Брюшина", callback_data="Brushina")],
               [types.InlineKeyboardButton(text="Верхний пищевар. отдел", callback_data="Verh_otdel")],
               [types.InlineKeyboardButton(text="Нижний пищевар. отдел", callback_data="Nij_otdel")],
               [types.InlineKeyboardButton(text="Пищевар. железы", callback_data="Pol_jen")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomia")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Sustavy():
    buttons = [[types.InlineKeyboardButton(text="Верхн. конеч. суставы", callback_data="Verh_kon_sustavy")],
               [types.InlineKeyboardButton(text="Ниж. конеч. суставы", callback_data="Nij_kon_sustavy")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_CNS():
    buttons = [[types.InlineKeyboardButton(text="Борозды. извилины. поля цнс", callback_data="Bor_izv_pol")],
               [types.InlineKeyboardButton(text="Пути цнс", callback_data="Puti")],
               [types.InlineKeyboardButton(text="Спинной мозг цнс", callback_data="Spin_mozg")],
               [types.InlineKeyboardButton(text="Ствол цнс", callback_data="Pol_jen")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Anatomia")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok1():
    buttons = [[types.InlineKeyboardButton(text="Клетка гист.", callback_data="Kletka")],
               [types.InlineKeyboardButton(text="Микрофото гист.", callback_data="Microfoto")],
               [types.InlineKeyboardButton(text="Окраски гист.", callback_data="Okraski")],
               [types.InlineKeyboardButton(text="Препараты 1 колок гист.", callback_data="Preparaty1")],
               [types.InlineKeyboardButton(text="Эмбриогенез", callback_data="Embriogenez")],
               [types.InlineKeyboardButton(text="Эпителий", callback_data="Epiteliy")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Gistologiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok2():
    buttons = [[types.InlineKeyboardButton(text="Кости гист.", callback_data="Kosti")],
               [types.InlineKeyboardButton(text="Кровь гист.", callback_data="Krov'")],
               [types.InlineKeyboardButton(text="Препараты 2 колок гист.", callback_data="Preparaty2")],
               [types.InlineKeyboardButton(text="Соединительные гист.", callback_data="Soedinitelnye")],
               [types.InlineKeyboardButton(text="Хрящи", callback_data="Hryashi")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Gistologiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok3():
    buttons = [[types.InlineKeyboardButton(text="Мышцы гист.", callback_data="MyshcyGista")],
               [types.InlineKeyboardButton(text="Препараты 3 колок гист.", callback_data="Preparaty3")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_Gistologiya")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_all_free():
    buttons = [[types.InlineKeyboardButton(text="Проводящие пути", callback_data="Provod_puti")],
               [types.InlineKeyboardButton(text="Промежность", callback_data="Promejnost'")],
               [types.InlineKeyboardButton(text="Ход брюшины", callback_data="Hod_brushiny")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_contents")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_all_webs():
    buttons = [[types.InlineKeyboardButton(text="Анатомия", callback_data="AnatomiyaWebs")],
               [types.InlineKeyboardButton(text="Биология", callback_data="BiologiyaWebs")],
               [types.InlineKeyboardButton(text="Гистология", callback_data="GistologiyaWebs")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_contents")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_AnatomiyaWebs():
    buttons = [[types.InlineKeyboardButton(text="Мочевыдел. сис. веб", callback_data="MochWeb")],
               [types.InlineKeyboardButton(text="Жен. пол. сис. веб", callback_data="Jen_polWeb")],
               [types.InlineKeyboardButton(text="Муж. пол. сис. веб", callback_data="Muj_polWeb")],
               [types.InlineKeyboardButton(text="Легкие веб", callback_data="LegkieWeb")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_BiologiyaWebs():
    buttons = [[types.InlineKeyboardButton(text="Вспомнить все био", callback_data="Vspomnit_vse_bioWeb")],
               [types.InlineKeyboardButton(text="Задачи по генетике", callback_data="GenetikaWeb")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_GistologiyaWebs():
    buttons = [[types.InlineKeyboardButton(text="Колок 1-й", callback_data="Colok1Web")],
               [types.InlineKeyboardButton(text="Колок 2-й", callback_data="Colok2Web")],
               [types.InlineKeyboardButton(text="Колок 3-й", callback_data="Colok3Web")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok1Web():
    buttons = [[types.InlineKeyboardButton(text="Эпителий веб", callback_data="EpiteliyWeb")],
               [types.InlineKeyboardButton(text="Эмбриогенез веб", callback_data="EmbriogenezWeb")],
               [types.InlineKeyboardButton(text="Клетка веб", callback_data="KletkaWeb")],
               [types.InlineKeyboardButton(text="Вспомнить все гист1", callback_data="Vspomnit_vse_colok1Web")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok2Web():
    buttons = [[types.InlineKeyboardButton(text="Кости веб", callback_data="KostiWeb")],
               [types.InlineKeyboardButton(text="Кровь веб", callback_data="KrovWeb")],
               [types.InlineKeyboardButton(text="Хрящи веб", callback_data="HryashiWeb")],
               [types.InlineKeyboardButton(text="Соединительные веб", callback_data="SoedinitelnyeWeb")],
               [types.InlineKeyboardButton(text="Вспомнить все гист2", callback_data="Vspomnit_vse_colok2Web")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_kb_Colok3Web():
    buttons = [[types.InlineKeyboardButton(text="Вспомнить все гист3", callback_data="Vspomnit_vse_colok3Web")],
               [types.InlineKeyboardButton(text="Назад", callback_data="Back_to_all_webs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
