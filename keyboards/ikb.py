from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


urlkb = InlineKeyboardMarkup(row_width=1)
ukb1 = InlineKeyboardButton(text='Открыть таблицу', url='https://docs.google.com/spreadsheets/d/1z0jLm4dVSaWQWw3aTD5ArVTgO-ylsYGQxC69XrFcMjM/edit#gid=0')
urlkb.add(ukb1)

