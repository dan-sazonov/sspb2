"""
Хэндлеры бота
Этот файл может содержать функции, отвечающие за визуальное отображение и валидацию данных, тексты сообщениий должны
лежать в файле `messages.py`.
"""

import config
import db
import santa

from dispatcher import dp, bot, storage
from messages import Messages
from aiogram import types

messages = Messages()
mes_santa = Messages.Santa()
db_main = db.Main()

santa.init()  # костыль, не трогать


async def on_startup(_):
    await config.set_commands(dp)
    await bot.send_message(chat_id=config.ADMIN_CHAT, text=messages.start_polling)


async def on_shutdown(_):
    await bot.close()
    await storage.close()
    await bot.send_message(chat_id=config.ADMIN_CHAT, text=messages.stop_polling)


@dp.message_handler(commands=['subscribe', 'start'])
async def start_mes(message: types.Message):
    await message.answer(messages.subscribe)
    await message.answer(messages.do_unsubscribe)
    db_main.add_user(int(message.from_user.id), message.from_user.username)
    db_main.update_counter(int(message.from_user.id), 'start')


@dp.message_handler(commands=['unsubscribe', 'stop'])
async def stop_mes(message: types.Message):
    db_main.update_counter(int(message.from_user.id), 'stop')
    db_main.del_user(int(message.from_user.id))
    await message.answer(messages.unsubscribe)
    await message.answer(messages.do_subscribe)


@dp.message_handler(commands=['help', '!', '?'])
async def help_mes(message: types.Message):
    await message.answer(messages.help, disable_web_page_preview=True)
    db_main.update_counter(int(message.from_user.id), 'help')


@dp.message_handler()
async def unknown_command_mes(message: types.Message):
    """
    Пересылаем все сообщения и айдишник юзеру, чисто для тестов
    Если эхо выключено, шлем сообщение, что команда не понятна

    :param message: Параметры сообщения, которое прилетело от юзера
    :return: None
    """
    if config.ENABLE_ECHO:
        await message.reply(message.text)
        await message.answer(f'usr id: {message.from_user.id}')
    else:
        await message.reply(messages.not_command)
