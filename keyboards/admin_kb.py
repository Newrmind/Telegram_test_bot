from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton('/Загрузить')
b2 = KeyboardButton('/Удалить')

kb_admin.add(b1, b2)