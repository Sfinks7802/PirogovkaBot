import asyncio
from aiogram import Dispatcher
from PrivatInfo import bot
from Handlers import cmd_start, payment, workinprogress_elements
from Filters.SubMiddleware import SubMiddleware


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router, payment.router, workinprogress_elements.router)
    dp.message.outer_middleware(SubMiddleware())
    dp.callback_query.outer_middleware(SubMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())