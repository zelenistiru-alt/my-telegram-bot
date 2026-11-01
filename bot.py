import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Токен вашего бота
API_TOKEN = '9118570537:AAE7pDlDbUMCAxicbO1_xV3chMFdsO4vJJU'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция создания главного меню
def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🔥 Новое о телеграмм")
    builder.button(text="🎵 Новое о Тикток")
    builder.button(text="📥 Новое о загрузке песен на Телеграмм")
    builder.adjust(2, 1) 
    return builder.as_markup(resize_keyboard=True)

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Что хотите узнать сегодня? 🤔",
        reply_markup=get_main_menu()
    )

# Обработка кнопки "🔥 Новое о телеграмм"
@dp.message(F.text == "🔥 Новое о телеграмм")
async def telegram_news(message: types.Message):
    await message.answer(
        "📢 Главные тренды и обновления Telegram:\n\n"
        "• Мини-приложения (Mini Apps): Бум Web3-игр прямо внутри чатов продолжается. Теперь они поддерживают полноэкранный режим и геолокацию.\n"
        "• Монетизация каналов: Авторы получают до 50% дохода от рекламы в своих каналах через Telegram Stars.\n"
        "• Улучшенные истории: Появилась возможность добавлять кастомную музыку и стикеры-реакции в сторис."
    )

# Обработка кнопки "🎵 Новое о Тикток"
@dp.message(F.text == "🎵 Новое о Тикток")
async def tiktok_news(message: types.Message):
    await message.answer(
        "📱 Что нового в мире TikTok:\n\n"
        "• Длинные видео: Платформа продвигает горизонтальные видео длительностью до 10-15 минут, конкурируя с YouTube.\n"
        "• Умные алгоритмы ИИ: Интеграция новых ИИ-эффектов для контента и автогенерация точных субтитров.\n"
        "• Внутренний поиск: TikTok заменяет поисковики для зумеров — пользователи ищут обзоры, рецепты и лайфхаки через поиск приложения."
    )

# Обработка кнопки "📥 Новое о загрузке песен на Телеграмм"
@dp.message(F.text == "📥 Новое о загрузке песен на Телеграмм")
async def music_download_news(message: types.Message):
    await message.answer(
        "⏱️ Новое о загрузке песен на Телеграмм:\n\n"
        "Следующие загрузки через день."
    )

# Главная функция запуска
async def main():
    print("Бот успешно запущен и ждет команду /start...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if name == 'main':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")
