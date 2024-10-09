import asyncio
from aiogram import Dispatcher
from Handlers import (cmd_start, gista_course, cq_contacts, cq_courses, cq_individual_courses,
                      cq_group_courses, cmd_my_materials, cq_all_contents, cmd_menu, cq_letniy_intensiv, bibla,
                      invoices, test, checklist, cnsint, cq_sersod_conspect, cq_vskint, anatint)
from Bot import bot


async def main():
    dp = Dispatcher()

    dp.include_routers(cmd_start.router, gista_course.router, cq_contacts.router,
                       cq_courses.router, cq_individual_courses.router, cq_group_courses.router, cmd_my_materials.router,
                       cq_all_contents.router, cmd_menu.router, cq_letniy_intensiv.router, bibla.router,
                       invoices.router, test.router, checklist.router, cnsint.router, cq_sersod_conspect.router, cq_vskint.router,
                       anatint.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())