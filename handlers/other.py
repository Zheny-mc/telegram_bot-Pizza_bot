from aiogram import types, Dispatcher
from create_bot import bot
import json
import string

async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation))
            for i in message.text.split(' ')}.intersection(set(json.load(open('cenzure.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()
    else:
        await message.answer(message.text)


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
