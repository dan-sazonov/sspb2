"""
Создает и настраивает бота
Все, что связано с обработкой сообщений, должно быть помещено в `handlers.py`.
"""
import logging
import config
import aiogram
import messages

from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Configure logging
logging.basicConfig(level=logging.INFO)

# кастомные костыльные логи
if config.ENABLE_ECHO:
    print('INFO: echo mode enable')

# init
TOKEN = config.API_TOKEN
bot = aiogram.Bot(token=TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
