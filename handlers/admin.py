from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from keyboards import kb_admin, get_inline_kb, INL_DELETE_COMMAND

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def make_chages_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Слушаю:', reply_markup=kb_admin)
    await message.delete()

# commands='Загрузить', state=None
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')

async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Отмена добавления пиццы')


# content_types=['photo'], state=FSMAdmin.photo
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название')

# state=FSMAdmin.name
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')


# state=FSMAdmin.description
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Укажи цену')


# state=FSMAdmin.price
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        await state.finish()


async def get_full_menu(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read_data_menu()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')

async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read_data_menu()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')
            await bot.send_message(message.from_user.id, text='\U0001F446', reply_markup=get_inline_kb(ret[1]))

async def del_callback_run(callback_query: types.CallbackQuery):
    pizza_name = callback_query.data.split('_')[1]
    await sqlite_db.sql_delete_command(pizza_name)
    await callback_query.answer(text=f'{pizza_name} удалена.', show_alert=True)

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(make_chages_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(get_full_menu, commands='Показать')
    dp.register_message_handler(delete_item, commands='Удалить')
    dp.register_callback_query_handler(del_callback_run, Text(startswith=INL_DELETE_COMMAND))

