import asyncio

from aiogram.utils.exceptions import MessageToDeleteNotFound
from aiogram import types

from config import MESSAGE_LIFETIME
from database import db


async def delete_message(message_id, chat_id, logger, bot):
    await asyncio.sleep(MESSAGE_LIFETIME)
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except MessageToDeleteNotFound as error:
        logger.error("Failed to delete message with ID %s: %s",
                     message_id, error)


async def start(message: types.Message):
    reply_text = '''Добро пожаловать! Я помогу вам хранить ваши пароли.

Поддерживаются следующие команды:
/set <сервис> <пароль> - добавляет пароль к сервису
/get <сервис> - получает пароль по названию сервиса
/del <сервис> - удаляет пароль для сервиса'''
    await message.reply(reply_text)


async def set_password(message: types.Message, logger, bot):
    user_id = message.from_user.id
    args = message.get_args().split(' ')
    if len(args) < 2:
        await message.reply('Используйте команду /set <сервис> <пароль>.')
        return
    service = args[0]
    password = ' '.join(args[1:])
    db.set_password(user_id, service, password)
    reply_text = "Пароль успешно сохранен.\n"
    reply_text += f"Сообщение с паролем будет удалено через {MESSAGE_LIFETIME} секунд."
    await message.reply(reply_text)
    asyncio.create_task(delete_message(message.message_id, message.chat.id,
                                       logger, bot))


async def get_password(message: types.Message, logger, bot):
    user_id = message.from_user.id
    args = message.get_args().split(' ')
    if len(args) < 1:
        await message.reply('Используйте команду /get <сервис>.')
        return
    service = args[0]
    result = db.get_password(user_id, service)
    if result:
        password = result[0]
        reply_text = f"Пароль для сервиса {service}: {password}\n"
        reply_text += f"Сообщение с паролем будет удалено через {MESSAGE_LIFETIME} секунд."
        reply_message = await message.reply(reply_text)
        asyncio.create_task(delete_message(reply_message.message_id,
                                           reply_message.chat.id,
                                           logger, bot))
        await asyncio.sleep(MESSAGE_LIFETIME)
        await message.delete()
    else:
        await message.reply('Пароль для указанного сервиса не найден.')


async def delete_password(message: types.Message):
    user_id = message.from_user.id
    args = message.get_args().split(' ')
    if len(args) < 1:
        await message.reply('Используйте команду /del <сервис>.')
        return
    service = args[0]
    db.delete_password(user_id, service)
    await message.reply(f'Пароль для сервиса {service} удален.')


async def unknown_command(message: types.Message):
    await message.reply('Неизвестная команда. Введите /help для списка команд.')
