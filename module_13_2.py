from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

# API токен вашего бота

api = "###   Здесь надо вводить токен Вашего бота (преподаватель сказал, что давать мне мой токен 'Vika' не надо   ###"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Функция для команды '/start'
# 1. start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
#    Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.reply("Привет! Я бот помогающий твоему здоровью.")

# Функция для сообщений с текстом "Vika" или "ff"
@dp.message_handler(text=['Vika', 'ff'])
async def vika_message(message: types.Message):
    print("Vika message")
    await message.reply("Это сообщение от 'Vika' или 'ff'.")

# Функция для обработки всех других сообщений
# 2. all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
# Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)

@dp.message_handler()
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен и готов к работе.")
    executor.start_polling(dp, skip_updates=True)

###   Вывод на консоль:
"""
Бот запущен и готов к работе.
Updates were skipped successfully.
Привет! Я бот помогающий твоему здоровью.
Vika message
"""