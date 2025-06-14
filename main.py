import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Импорт конфигурации токена и роутеров
from config import BOT_TOKEN
from routers.start import start_router
from routers.cat import cat_router
from routers.weather import weather_router
from routers.photo import photo_router
from routers.translate import translate_router
from routers.nasa import nasa_router
# from db.users import init_db  # Функция инициализации БД

# === НАСТРОЙКА ЛОГГЕРА ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()  # Используем in-memory хранилище состояний (можно заменить на Redis)
dp = Dispatcher(storage=storage)

async def main():
    # Инициализация базы данных
    # init_db()

    # Подключение всех роутеров
    dp.include_router(start_router)
    dp.include_router(weather_router)
    dp.include_router(photo_router)
    dp.include_router(translate_router)
    dp.include_router(cat_router)
    dp.include_router(nasa_router)

    logger.info("Бот запущен")
    # Запуск polling (постоянное получение апдейтов)
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
