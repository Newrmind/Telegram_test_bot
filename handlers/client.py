from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

import random

'''Для того, чтобы в хендлерах улавливать сообщения с конкретным текстом в aiogram есть специальный фильтр:
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(equals='Начать работу',
                         ignone_case=True)) # игнорировать регистр
async def start_cmd(message: types.Message):
'''


HELP_COMMAND = """
<b>/start</> - <em>старт бота</em>
<b>/help</> - <em>список команд</em>
<b>/description</> - <em>описание бота</em>
<b>/send_photo</> - <em>отправка фото</em>
<b>/send_random</> - <em>отправка случайного числа</em>
<b>/menu</> - <em>показать меню пиццерии</em>
"""

async def start_command(message: types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Добро пожаловать в главное меню\n{HELP_COMMAND}',
                               parse_mode='HTML',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Verdelet_bot ')


async def command_send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://s1.eda.ru/StaticContent/Photos/120131085053/171027192707/p_O.jpg')


async def send_random_num_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=str(random.randint(1, 1000)))


async def send_description(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Наш бот классный!',
                           reply_markup=ReplyKeyboardRemove())

async def send_menu(message: types.Message):
    await sqlite_db.sql_read(message)


# Убираем декораторы и регистрируем обработку команд в отдельной функции
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(command_send_photo, commands=['send_photo'])
    dp.register_message_handler(send_random_num_command, commands=['send_random'])
    dp.register_message_handler(send_description, commands=['description'])
    dp.register_message_handler(send_menu, commands=['menu'])