from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from app.otz import CheckLavozim
from app.getData import GetHRP
import requests
import pandas as pd
router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hush kelibsiz. Quyidagi xizmatlardan birini tanlang", reply_markup= await kb.get_main_keyboard())


@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

@router.message(F.text == "Orqara")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




@router.message(F.text == "OTZ")
async def otz_command(message: Message):
    await message.answer("Quyidagilardan birini tanlang!", reply_markup= await kb.otz_keyboard())


@router.message(F.text == 'Lavozim')

async def lavozim_command(message: Message):
    TOKEN = "4620|xDz0N9JvIiMBB7TQYQwSmqar7cbXKjTIDo9eU4ha"
    url = "https://b-hr.uzautomotors.com/api/position-description-detail"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    # response = requests.get("https://b-hr.uzautomotors.com/api/test")
    response = requests.get(url, headers=headers)

    # print("Status:", response.status_code)
    # print("Text:", response.text)
    if response.headers.get("Content-Type", "").startswith("application/json"):
        data = response.json()
        if data:
            df_yoqlar = pd.DataFrame(data['not_exist_position_description'])
            df_borlar = pd.DataFrame(data['exist_position_description'])
            jami = len(df_borlar)+ len(df_yoqlar)
            # Summarize the DataFrames to avoid long messages
            borlar_count = len(df_borlar)
            yoqlar_count = len(df_yoqlar)
            await message.answer(
                f"Lavozim yo'riqnomalar bo'yicha ma'lumotlar:\n"
                f"Jami: {jami}\n"
                f"Borlari soni: {borlar_count}\n"
                f"Yo'qlari soni: {yoqlar_count}"
            )
        else:
            await message.answer("JSON ma'lumotlar topilmadi.")
    else:
        print("JSON emas:", response.text)
    # await message.answer(f"response: \n {response.text}", reply_markup= await kb.otz_keyboard())
    # await message.answer("response: \n ", reply_markup= await kb.otz_keyboard())
