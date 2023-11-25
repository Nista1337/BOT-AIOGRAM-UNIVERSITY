import asyncio
from utils.set_bot_commands import set_default_commands
import logging
import handlers
import data
import data.config as config
from aiogram import Bot, Dispatcher
from loader import router


async def on_startup():
    bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()



    await bot.delete_webhook(drop_pending_updates=True)
    await set_default_commands(bot)
    dp.include_router(router=router)
    await dp.start_polling(bot)


    


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(on_startup())
    except Exception as err:
        logging.exception(err)

