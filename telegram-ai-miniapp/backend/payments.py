from aiogram.types import LabeledPrice
from bot import bot


async def create_invoice(user_id, amount):

    prices = [LabeledPrice(label="Stars", amount=amount)]

    await bot.send_invoice(

        chat_id=user_id,

        title="Deposit",

        description=f"{amount} Stars",

        provider_token="",

        currency="XTR",

        prices=prices,

        payload="deposit"
    )