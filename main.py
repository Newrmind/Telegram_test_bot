from aiogram import executor

from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp) # тут пустой хендлер, поэтому он должен располагаться в самом низу!!!


async def on_startup(_):
    print('Bot started successfully!')
    sqlite_db.sql_start() # Функция запуска базы данных


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

