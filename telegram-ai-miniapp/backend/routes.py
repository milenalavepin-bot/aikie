from fastapi import APIRouter
import database
from generators.image import generate_image
from generators.video import generate_video
import config

router = APIRouter()


@router.get("/profile/{user_id}")
async def profile(user_id:int):

    balance = database.get_balance(user_id)

    return {"balance":balance}


@router.get("/history/{user_id}")
async def history(user_id:int):

    return database.get_history(user_id)


@router.post("/generate-image")
async def gen_image(data:dict):

    user_id=data["user_id"]
    prompt=data["prompt"]

    balance=database.get_balance(user_id)

    if balance < config.IMAGE_PRICE:

        return {"error":"not enough balance"}

    url=await generate_image(prompt)

    database.deduct_balance(user_id, config.IMAGE_PRICE)

    database.save_history(user_id,"image",prompt,url)

    return {"url":url}


@router.post("/generate-video")
async def gen_video(data:dict):

    user_id=data["user_id"]
    prompt=data["prompt"]

    balance=database.get_balance(user_id)

    if balance < config.VIDEO_PRICE:

        return {"error":"not enough balance"}

    url=await generate_video(prompt)

    database.deduct_balance(user_id, config.VIDEO_PRICE)

    database.save_history(user_id,"video",prompt,url)

    return {"url":url}