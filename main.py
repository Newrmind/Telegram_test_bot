import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

bot = Bot(os.getenv('BOT_API'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot started successfully!')

async def test_func() -> str:
    print('TEXT')

test_func()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню')

@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer(text='Choice option...!')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

