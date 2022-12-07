from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text


ID = None
class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Получаем ID текущего модератора
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you need?!!!')

# Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID: # Проверяем, является ли пользователь администратором
        await FSMAdmin.photo.set() # бот перейдёт в режим работы FSM машины состояний и будет ждать загрузки фото
        await message.reply('Загрузи фото')
    else:
        await message.reply('Пройдите проверку на наличие прав администратора!')

# Выход из машины состояний
#@dp.message_handler(state="*", commands='Отмена') # state="*" означает любое состояние FSM
#@dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        concurrent_state = await state.get_state()
        if concurrent_state is None:
            return
        await state.finish()
        await message.reply('OK')


# Ловим первый ответ от пользователя и пишем в словарь
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    # Из сообщения фото по индексу 0 получаем id картинки, который потом и будет записываться в БД, чтобы не сохранять саму картинку
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            # переводим FSM машину состояний в режим ожидания следующего ответа
            await FSMAdmin.next()
            await message.reply('Теперь введи название')

# Ловим второй ответ от пользователя
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text # получаем текст сообщения и записываем в словарь
            # переводим FSM машину состояний в режим ожидания следующего ответа
            await FSMAdmin.next()
            await message.reply('Теперь введи описание')

# Ловим третий ответ от пользователя
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text # получаем текст сообщения и записываем в словарь
            # переводим FSM машину состояний в режим ожидания следующего ответа
            await FSMAdmin.next()
            await message.reply('Теперь укажи цену')

# Ловим четвёртый ответ от пользователя
#@dp.message_handler(content_types=['price'], state=FSMAdmin.description)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text) # получаем текст сообщения, переводим в число с плавающей точкой и записываем в словарь

        # Выведем собранные данные в сообщении
        async with state.proxy() as data:
            await message.reply(str(data))

            # завершаем работу FSM машины состояний
            # В результате выполнения команды state.finish() все собранные данные будут удалены, поэтому все действия с данными
            # необходимо произвести до вызова данной команды!!!
            await state.finish()



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)