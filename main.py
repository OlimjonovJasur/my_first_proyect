from aiogram import Bot, Dispatcher  # bot bilan bo'g'lanish uchun bot sinfi, dispatcher => boshqaruvchi types => habarlar bilan ishlash uchun
from asyncio import run     # asinxron fnksiyani ishga tushurish uchun run funksiyasini ishga tushuramiz

from funksiyalar import get_user_info

dp = Dispatcher()    # Dispatcher obyektini yaratish boshqaruvchi obyekt
bot = Bot("7461068423:AAEMPMS1nx86hGfxPj4PwM6vHIQ4PoAU8Dc")  # bot tokeni


async  def startup_answer(bot: Bot):
    await bot.send_message(5667145916, "Bot ishga tushdi🥶🥶🥶")


async def shutdown_answer(bot: Bot):
    await bot.send_message(5667145916, "bot ishdan to'xtadi⚙️⚙️⚙️")


# async botni ishga tushurish uchun ishlatiladi
async def start():
    dp.startup.register(startup_answer)      # bot bajaradigon ilk ish
    dp.message.register(get_user_info)  # echo botni ishga tushurish uchun ishlatiladi
    dp.shutdown.register(shutdown_answer)     # chiqib ketish toxtatish desaham bo'ladi

    await dp.start_polling(bot, polling_timeout=1)            # asinxron metodni ishga tushuramiz
# polling_timeout bu siz telegramga yozsangiz undan qancha vaqtda xabar kelishini berasiz.


run(start())









