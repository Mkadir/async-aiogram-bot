from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from datas import config

bot = Bot(token=config.bot_token, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage() 

# Configure logging
logging.basicConfig(level=logging.INFO)


dp = Dispatcher(bot, storage=storage)