from aiogram.utils import executor
from createBot import dp
from DataBase import Data_Base


async def on_startup(_):
    print('Бот готов к работе!')
    Data_Base.sql_start()


from handlers import command, FSM, FSM_post_description, FSM_post_name, other

command.register_hadnlers_client(dp)
FSM.register_hadnlers_FSM(dp)
FSM_post_description.register_hadnlers_FSM_description(dp)
FSM_post_name.register_hadnlers_FSM_name(dp)
other.register_hadnlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)