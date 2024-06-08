import asyncio
from aiogram import Dispatcher
from PrrivatInfo import bot
from Handlers import cmd_start


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())