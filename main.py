from aiogram import executor
from create_bot import dp

from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp) # тут пустой хендлер, поэтому он должен располагаться ниже

async def on_startup(_):
    print('Bot started successfully!')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

