from aiogram import Bot
from aiogram.dispatcher import Dispatcher

with open('token.txt') as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
