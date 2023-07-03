import sqlite3
from createBot import bot


def sql_start():
    global db
    global cursor
    db = sqlite3.connect('mydb.db')
    cursor = db.cursor()
    if db:
        print('Таблица подлючена!')
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Posts(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)""")
    db.commit()


async def sql_read(message):
    for i in cursor.execute(f""" SELECT name, id AS id FROM Posts ORDER BY id LIMIT 5 """).fetchall():
        await bot.send_message(message.from_user.id, f"{i[1]}: {i[0]}")


async def sql_number_description(message):
    for descript in cursor.execute(f""" SELECT description FROM Posts WHERE id = {message.text} """).fetchall():
        for el in descript:
            try:
                await bot.send_message(message.from_user.id, el[:950])
                await bot.send_message(message.from_user.id, el[1000:])
                await bot.send_message(message.from_user.id, el[5000:9000])
                await bot.send_message(message.from_user.id, el[9000:])
            except:
                await bot.send_message(message.from_user.id, '<b>Конец статьи!</b>', parse_mode='html')


async def sql_number_name(message):
    for name in cursor.execute(f""" SELECT name FROM Posts WHERE id = {message.text} """).fetchall():
        for el in name:
            await bot.send_message(message.from_user.id, el)


async def sql_post_delete(message):
    pass
