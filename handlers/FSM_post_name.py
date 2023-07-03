from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from DataBase import Data_Base

class FSMadmin_name(StatesGroup):
    number = State()

# @dp.message_handler(commands=['название'], state=None)
async def cm_start(message: types.Message):
    await FSMadmin_name.number.set()
    await message.answer('Напиши номер статьи')
    await message.delete()


# @dp.message_handler(content_types=['text'], state=FSMadmin_name.number)
async def load_name(message: types.Message, state: FSMContext):
    num_post = message
    await Data_Base.sql_number_name(num_post)
    await state.finish()


def register_hadnlers_FSM_name(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['название'], state=None)
    dp.register_message_handler(load_name, state=FSMadmin_name.number)