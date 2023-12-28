from aiogram import Bot, Dispatcher
import asyncio
import logging
from config import BOT_TOKEN
from app.handlers import router
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

async def main():
    global dp,bot
    print(BOT_TOKEN)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    # print('start')
    logging.basicConfig(level=logging.DEBUG)
    # try:
    asyncio.run(main())
    # except KeyboardInterrupt:
    # print("exit")

