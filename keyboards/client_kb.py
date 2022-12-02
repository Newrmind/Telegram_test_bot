from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,)
                                #one_time_keyboard=True) #Сворачиваем клавиатуру

b1 = KeyboardButton('/description')
b2 = KeyboardButton('/send_photo')
b3 = KeyboardButton('/send_random')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить моё местоположение', request_location=True)

kb_client.add(b1, b2).add(b3)#.row(b4, b5)