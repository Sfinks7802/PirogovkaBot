import asyncio
import os
from aiogram import Dispatcher
from Handlers import cmd_start, payment, workinprogress_elements, cq_contacts
from Filters.SubMiddleware import SubMiddleware
from Bot import bot


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router, payment.router, workinprogress_elements.router, cq_contacts.router)
    dp.message.outer_middleware(SubMiddleware())
    dp.callback_query.outer_middleware(SubMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())