from aiogram import types

all_contents_names = {

}


def get_kb_contents(contents):
    buttons = []
    for content in contents:
        buttons.append([types.InlineKeyboardButton(text=f'{all_contents_names[f"{content}"]}', callback_data=f'{content}')])
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_payed_content(content_name):
    return open(f'{content_name}.pdf' + '.pdf', 'rb')