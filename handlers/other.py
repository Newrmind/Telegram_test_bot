from aiogram import types, Dispatcher
import string


async def words_filter(message: types.Message):
    #Получаем сообщение, разбиваем по разделителю пробел на слова, отфильтровываем из слов знаки препинания и спецсимволы
    for i in {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}:
        if i in ['мат']:
            await message.reply('Мат запрещён!')
            await message.delete()


# Убираем декораторы и регистрируем обработку команд в отдельной функции
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(words_filter)