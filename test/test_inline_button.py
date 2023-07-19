from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

with open('../token.txt') as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# url_kb = InlineKeyboardMarkup(row_width=4)
# url_button = InlineKeyboardButton(text='ютуб', url='https://www.youtube.com/')
# url_button2 = InlineKeyboardButton(text='гугл', url='https://www.google.com/?hl=Ru')
# url_kb.add(url_button, url_button2)
#
# # инлайн сслыки
# create_button = lambda text, url: InlineKeyboardButton(text=text, url=url)
# text_button = (('ютуб1', 'https://www.youtube.com/'),
#                ('ютуб2', 'https://www.youtube.com/'),
#                ('ютуб3', 'https://www.youtube.com/'))
#
# url_buttons = [create_button(i[0], i[1]) for i in text_button]
# url_kb.row(*url_buttons)
#
# url_kb.insert(create_button('google2', 'https://www.google.com/'))
#
# @dp.message_handler(commands='ссылки')
# async def url_command(message: types.Message):
#     await message.answer('Links: ', reply_markup=url_kb)


# инлайн кнопки

lst_human = {}
question = {True: 0, False: 0}
NAME_COMMAND = 'like_'


in_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data=f'{NAME_COMMAND}1'),
                                              InlineKeyboardButton(text='DizLike', callback_data=f'{NAME_COMMAND}-1'))

@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('Inline button:', reply_markup=in_kb)

@dp.callback_query_handler(Text(startswith=NAME_COMMAND))
async def www_cal(callback_message: types.CallbackQuery):
    res = int(callback_message.data.split('_')[1])
    user_id = f'callback_message.from_user.id'
    if user_id not in lst_human:
        lst_human[user_id] = res > 0
        question[res > 0] += 1
        await callback_message.answer('Вы проголосовали!')
    else:
        await callback_message.answer('Вы уже проголосовали!')

# await callback_message.answer()
# await callback_message.answer('Кнопка нажата', show_alert=True)




executor.start_polling(dp, skip_updates=True)