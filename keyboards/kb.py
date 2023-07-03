from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/загрузить')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/отмена')
b4 = KeyboardButton('/список')
b5 = KeyboardButton('/название')
b6 = KeyboardButton('/статья')
b7 = KeyboardButton('/удалить_пост')
b10 = KeyboardButton('/таблица')

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb.add(b2).row(b1, b3).add(b4).add(b5, b6).add(b7).add(b10)
