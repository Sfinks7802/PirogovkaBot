from aiogram import types

 
def get_kb_for_sub():
    buttons = [[types.InlineKeyboardButton(text="Эксклюзивно РНИМУ", callback_data="bibla")],
               # [types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
               [types.InlineKeyboardButton(text='Репетиторы', callback_data='courses')],
               [types.InlineKeyboardButton(text='Материалы от Пироговки', callback_data='Pirogovka_matirials')]]
               # [types.InlineKeyboardButton(text='Мои материалы', callback_data='my_materials')],
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_for_sub_guide_v2():
    buttons = [[types.InlineKeyboardButton(text="👉 Хочу узнать, как это работает", callback_data="guide_v2_intro")],
               [types.InlineKeyboardButton(text='📘 Уже слышал(а) про гайд', callback_data='guide_v2_fasttrack')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_Pirogovka_matirials():
    buttons = [
        # [types.InlineKeyboardButton(text='Гайд по учебе', callback_data='letniy_intensiv')],
        [types.InlineKeyboardButton(text='Контакты', callback_data='contacts')],
        [types.InlineKeyboardButton(text='Конспекты', callback_data='pirogovka_conspects')],
        [types.InlineKeyboardButton(text='ТА и ОПХ', url='https://drive.google.com/drive/folders/1pUWY5VNvPxq-WKubL3PxdMgpCtYrfUM0')],
        [types.InlineKeyboardButton(text='Вспомнить всё 5', callback_data='remember5_1')],
        [types.InlineKeyboardButton(text='Вспомнить всё 1', callback_data='remember1_1')],
        [types.InlineKeyboardButton(text='Общая гистология', callback_data='web_obsh_gist')],
        [types.InlineKeyboardButton(text='Веб хрящевые', callback_data='web_hrash')],
        [types.InlineKeyboardButton(text='Веб костные', callback_data='web_kosty')],
        [types.InlineKeyboardButton(text='Вспомнить всё 6', callback_data='remember6')],
        [types.InlineKeyboardButton(text='Вспомнить всё 2', callback_data='remember2')],
        [types.InlineKeyboardButton(text='Вспомнить всё 3', callback_data='remember3')],
        [types.InlineKeyboardButton(text='Вспомнить всё 7', callback_data='remember7')],
        [types.InlineKeyboardButton(text='Веб нервы', callback_data='web_nervy')],
        [types.InlineKeyboardButton(text='Интенсив по ЦНС (новый)', callback_data='intensiv_cns')],
        [types.InlineKeyboardButton(text='ВЕБИНАР ПИЩЕВАРИТЕЛЬНАЯ 1', callback_data='pishevar1')],
        [types.InlineKeyboardButton(text='Веб по эпителию', callback_data='epitely')],
        # [types.InlineKeyboardButton(text='Вспомнить всё 4', callback_data='vskint')],
        # [types.InlineKeyboardButton(text='Вспомнить всё 5', callback_data='remember5')],
        # [types.InlineKeyboardButton(text='Вспомнить всё 1', callback_data='remember1')],
        [types.InlineKeyboardButton(text='Интенсив ЦНС', callback_data='cnsint')],
        [types.InlineKeyboardButton(text='Чеклист по покупкам', callback_data='checklist')],
        #[types.InlineKeyboardButton(text="Курс по гистологии", callback_data="gist_course")],
        [types.InlineKeyboardButton(text="Экзамен по гистологии", callback_data="gist_ekz")],
        [types.InlineKeyboardButton(text="Экзамен по анатомии", callback_data="anat_ekz")],
        [types.InlineKeyboardButton(text="Задачи к экзамену", callback_data="zadachi")],
        [types.InlineKeyboardButton(text="Веб по нервной системе", callback_data="nervnaya_sys")],
        [types.InlineKeyboardButton(text="Окраски и микроскоп", callback_data="okraski")],
        [types.InlineKeyboardButton(text="Методы окраски в гистологии", callback_data="okraski_conspect")],
        [types.InlineKeyboardButton(text="Введение + ротовая полость", callback_data="rotpol")],
        [types.InlineKeyboardButton(text="Клеточная поверхность", callback_data="klet_poverh")],
        [types.InlineKeyboardButton(text="Органы чувств", callback_data="org_chuv")],
        [types.InlineKeyboardButton(text="Гайд 'Успешный студент-медик'", callback_data="time_guide")],
        #         # [types.InlineKeyboardButton(text='Конспекты_Пироговка', callback_data='all_contents')],
        [types.InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_kb_pirogovka_conspects():
    buttons = [
        [types.InlineKeyboardButton(text='Конспект сердечно-сосуд. сис.', callback_data='SerSod_conspect')],
        [types.InlineKeyboardButton(text='Анатомия. Черепно-мозговые нервы', callback_data='anatint')],
        [types.InlineKeyboardButton(text='Эмбриогенез', callback_data='Embriogenez_conspect')],
        [types.InlineKeyboardButton(text='Назад', callback_data='Pirogovka_matirials')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

