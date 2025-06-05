from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
import pandas as pd


from apscheduler.schedulers.asyncio import AsyncIOScheduler



router = Router()




@router.message(Command('start'))
async def start_command(message: Message):#,roles: list[str]
    # await message.answer(f"Sizning Telegram ID: {message.from_user.id}")
    await message.answer(f"Hush kelibsiz, {message.from_user.full_name}!", reply_markup=await kb.get_main_keyboard())


@router.message(Command('admin'))
async def admin_command(message: Message, roles: list[str]):
    if  'admin' in roles:
        await message.answer("Admin panelga xush kelibsiz!", reply_markup=await kb.get_main_keyboard())
    else:
        await message.answer("Kechirasiz, bu bo'lim faqat adminlar uchun", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

@router.message(F.text == "Orqaga")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




   







    