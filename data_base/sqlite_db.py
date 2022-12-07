import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('pizza_bot.db')
    cur = base.cursor()
    # При успешном подключении к бд выводим сообщение об этом
    if base:
        print('Database connection successful!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price INT)')
    base.commit()

# Функция для внесения данных в бд
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()

# Функция для чтения данных из бд
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall(): # Получаем список строк таблицы, перебираем в цикле каждую строку.
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

