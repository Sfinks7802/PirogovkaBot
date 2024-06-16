import asyncio
import os
from aiogram import Dispatcher
from Handlers import (cmd_start, payment, workinprogress_elements, cq_contacts, cq_courses, cq_individual_courses,
                      cq_group_courses)
from Filters.SubMiddleware import SubMiddleware
from Bot import bot


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router, payment.router, workinprogress_elements.router, cq_contacts.router, 
                       cq_courses.router, cq_individual_courses.router, cq_group_courses.router)
    dp.message.outer_middleware(SubMiddleware())
    dp.callback_query.outer_middleware(SubMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())