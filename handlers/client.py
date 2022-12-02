from aiogram import types, Dispatcher
from create_bot import dp, bot
import random


async def start_command(message: types.Message):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Добро пожаловать в главное меню',)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Verdelet_bot ')


async def command_send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://s1.eda.ru/StaticContent/Photos/120131085053/171027192707/p_O.jpg')


async def send_random_num_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=str(random.randint(1, 1000)))


# Убираем декораторы и регистрируем обработку команд в отдельной функции
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(command_send_photo, commands=['send_photo'])
    dp.register_message_handler(send_random_num_command, commands=['send_random'])