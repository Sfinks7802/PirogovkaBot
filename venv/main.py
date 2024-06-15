import asyncio
from aiogram import Dispatcher
from PrivatInfo import bot
from Handlers import cmd_start, payment


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router, payment.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())