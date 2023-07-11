from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Мое расположение', request_location=True)
# b5 = KeyboardButton('Мой номер', request_contact=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True # скрыть клаву
kb_client.add(b1).add(b2).add(b3)
# kb_client.add(b1).add(b2).add(b3).row(b4, b5)
# kb_client.row(b1, b2, b3)
# kb_client.add(b1).add(b2).insert(b3)


