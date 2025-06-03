import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from otz.handlers import otzrouter
from app.db import init_db
# from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from app.middlewares import RoleMiddleware






async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # init_db()
    dp.message.middleware(RoleMiddleware())
    dp.include_router(otzrouter)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting....")