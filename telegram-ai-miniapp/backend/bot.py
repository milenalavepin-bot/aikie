from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, LabeledPrice
from aiogram.filters import CommandStart
import asyncio

import config
import database

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):

    database.create_user(
        message.from_user.id,
        message.from_user.username
    )

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="🚀 Open App",
                    web_app=WebAppInfo(
                        url=config.BASE_URL
                    )
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Open AI Generator",
        reply_markup=kb
    )


async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())