# Вместо текущих цифр вставить ID человека, который создал бота
# Чтобы узнать свой айди, напиши этому - https://t.me/getmyid_bot боту команду start
ADMIN_CHAT = 385056286

# Вместо @dan_sazonov - логин телеги человека, который ответственный за бот, и если что, поможет с регистрацией
# Обязательно в кавычках
QA_CHAT = '@dan_sazonov'

# Меняем в кавычках на дату, когда пройдет встреча с обменом подарками
MEETING_DATE = '18 декабря'

# В кавычки вставить токен бота, который скинул BotFather
API_TOKEN = ''


# НИЖЕ ЭТОЙ СТРОЧКИ НИЧЕГО НЕ ТРОГАТЬ!!!
########################################

"""
Файл с конфигами бота
Здесь задаем глобальные константы и возможно функции, настраивающие (((что-то))).
"Why not json/csv/yaml/something else? - Fuck you, here's why".
"""
import os

from aiogram import types

ADMIN_ID = {ADMIN_CHAT, }

ENABLE_ECHO = False  # все команды будут попадать в эхо

# prerequisites
# в рот я этот DRY, скажи спасибо, что вообще работает

DB_USR = 'postgres'
DB_PASS = 'root'

# API_TOKEN = os.getenv('BOT_TOKEN')
if not API_TOKEN:
    # exit('Err: BOT_TOKEN variable is missing')
    print('Err: BOT_TOKEN variable is missing')

# DB_USR = os.getenv('DB_TEST_USR')
if not DB_USR:
    exit('Err: DB_USR variable is missing')

# DB_PASS = os.getenv('DB_TEST_PASS')
if not DB_PASS:
    exit('Err: DB_PASS variable is missing')


async def set_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('santa', 'Тайный Санта - регистрация'),
        types.BotCommand('end', 'Тайный Санта - выход из игры'),
        types.BotCommand('help', 'Краткая справка'),
        types.BotCommand('stop', 'Остановить бота и удалить всю информацию о себе')
    ])
