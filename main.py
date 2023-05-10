import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import handlers

from config import TOKEN
from database import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(handlers.start, commands=['start'])
dp.register_message_handler(lambda message:
                            handlers.set_password(message, logger, bot),
                            commands=['set'])
dp.register_message_handler(lambda message:
                            handlers.get_password(message, logger, bot),
                            commands=['get'])
dp.register_message_handler(handlers.delete_password, commands=['del'])
dp.register_message_handler(handlers.unknown_command)


async def main():
    db.create_table()
    await dp.start_polling()
    logger.info('Bot started')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
