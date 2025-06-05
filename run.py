import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from otz.handlers import otzrouter
from otz.auto_send import send_daily_mmb
from kadr.handlers import kadrrouter
from kadr.auto_send import send_daily_kadr
from app.db import init_db
# from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from app.middlewares import RoleMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import logging



# Loggerni sozlash
logging.basicConfig(level=logging.INFO)

# Scheduler
scheduler = AsyncIOScheduler()




async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # init_db()
    dp.message.middleware(RoleMiddleware())
    dp.include_router(kadrrouter)
    dp.include_router(otzrouter)
    dp.include_router(router)

    # Ish kunlari (dushanba-juma), soat 18:33 da ishga tushadi
    scheduler.add_job(
        send_daily_mmb,  # Pass the function, not the awaited result
        CronTrigger(day_of_week='mon-fri', hour=10, minute=0, timezone='Asia/Tashkent'),
        args=[bot]  # Pass bot as argument
    )
    scheduler.add_job(
        send_daily_kadr,  # Pass the function, not the awaited result
        CronTrigger(day_of_week='mon-fri', hour=9, minute=0, timezone='Asia/Tashkent'),
        args=[bot]  # Pass bot as argument
    )


    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting....")