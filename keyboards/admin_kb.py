from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_get = KeyboardButton('/Показать')
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(button_get).add(button_load).add(button_delete)


INL_DELETE_COMMAND = 'удалить_'
def get_inline_kb(name_pizza: str):
    return InlineKeyboardMarkup(row_width=1)\
        .add(InlineKeyboardButton(text=f'Удалить {name_pizza}',
                                  callback_data=f'{INL_DELETE_COMMAND}{name_pizza}'))