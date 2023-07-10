from aiogram.utils import executor
from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher

with open('../token.txt') as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в онлайн')

@dp.message_handler(commands=['start', 'help'])
async def start_command(message : types.Message):
    await message.answer('Привет')

@dp.message_handler(commands=['command'])
async def echo(message : types.Message):
    await message.answer(message.text)

@dp.message_handler(lambda message: 'такси' in message.text)
async def taxi(message: types.Message):
    await message.answer('такси')

@dp.message_handler(lambda message: message.text.startswith('нло'))
async def NLO(message: types.Message):
    await message.answer(message.text[:3])

@dp.message_handler()
async def empty(message : types.Message):
    # await message.answer('Нет такой команды')
    await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)