from loader import dp , bot
from aiogram import types
import logging 
@dp.message_handler(text='/start')
async def start_command(message:types.Message):
    await  message.answer(f"Hello {message.from_user.first_name}")
