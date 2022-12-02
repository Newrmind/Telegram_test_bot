import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


load_dotenv()

bot = Bot(os.getenv('BOT_API'))
dp = Dispatcher(bot)