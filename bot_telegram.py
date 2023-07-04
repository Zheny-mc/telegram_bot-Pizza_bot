from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

with open('token.txt') as f:
    TOKEN = f.readline().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message :types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)