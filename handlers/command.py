from aiogram import types, Dispatcher
from createBot import dp, bot
from keyboards import kb, urlkb
from DataBase import Data_Base



async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот!', reply_markup=kb)
    await message.delete()


# @dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'<b>Таблица</b> - список объявлений\n'
                                                 f'<b><i>Выгрузка объявление:</i></b>\n'
                                                 f'<b>Загрузить</b> - пошаговое создание поста\n'
                                                 f'<b>Отмена</b> - выход из процесса создания поста', parse_mode='html')
    await message.delete()


# @dp.message_handler(commands=['таблица'])
async def table(message: types.Message):
    await bot.send_message(message.from_user.id, '👁 Таблица объявлений ✍️', reply_markup=urlkb)
    await message.delete()


# @dp.message_handler(commands=['список'])
async def read_db(message: types.Message):
    await Data_Base.sql_read(message)






def register_hadnlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(table, commands=['таблица'])
    dp.register_message_handler(read_db, commands=['список'])
