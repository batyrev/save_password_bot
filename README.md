# save_password_bot

## Overview
Мы каждый день пользуемся большим количеством разных сервисов и зачастую, для каждого из них, требуются логин и пароль. А наш мозг отказывается запомнить их все... Поэтому был реализован Telegram бот, который обладает функционалом персонального хранилища паролей. 

Поддерживаются следующие команды:
- /set <string: key> <string: value> - добавляет пароль к сервису
- /get <string: key> - получает пароль по названию сервиса
- /del <string: key> - удаляет пароль для сервиса

## Requirements
Python 3.9.0+

## Usage
Запуск бота.

Установка зависимостей:
```
pip install -r requirements.txt
```

Запуск main.py с параметрами --token (обязательный) и --deltime (по-умолчанию: 10 сек).
```
python main.py --token <string:TOKEN> --deltime <int:MESSAGE_LIFETIME>
```
При этом в приоритете - переменные окружения! (Только если нет переменных окружения TOKEN и MESSAGE_LIFETIME, используются переданные параметры).

## Running with Docker

```bash
# building the image
docker build -t save_password_bot .

# starting up a container
docker run -e TOKEN="TOKEN" -e MESSAGE_LIFETIME="MESSAGE_LIFETIME" save_password_bot

```