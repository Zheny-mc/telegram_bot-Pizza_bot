import sqlite3 as sq
from create_bot import bot
from aiogram import types

SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)'
SQL_INSERT = 'INSERT INTO menu VALUES (?, ?, ?, ?)'
SQL_SELECT = 'SELECT * FROM menu'

def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('DataBase connected OK!')
    base.execute(SQL_CREATE_TABLE)
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute(SQL_INSERT, tuple(data.values()) )
        base.commit()

async def sql_read_menu(message: types.Message):
    for ret in cur.execute(SQL_SELECT).fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')

