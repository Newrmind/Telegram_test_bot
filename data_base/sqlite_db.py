import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('pizza_bot_db')
    cur = base.cursor()
    # При успешном подключении к бд выводим сообщение об этом
    if base:
        print('Database connection successful!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()