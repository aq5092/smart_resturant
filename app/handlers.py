from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
import pandas as pd
from db import is_user_registered, register_user
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

#group id -1002533887342
REQUIRED_GROUP_ID = -1002533887342

router = Router()


async def is_user_in_group(bot, user_id: int, group_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=group_id, user_id=user_id)
        return member.status in ["member", "creator", "administrator"]
    except TelegramBadRequest:
        return False


@router.message(CommandStart())
async def start_command(message: Message, bot: Bot):
    telegram_id = message.from_user.id
    
    # if message.chat.type in ["HR takliflar", "supergroup", 'group']:
    #     await message.answer(f"Guruh ID: `{message.chat.id}`", parse_mode="Markdown")
        # print(message.chat.id)

    # Guruhga a'zo ekanligini tekshir
    is_member = await is_user_in_group(bot, telegram_id, REQUIRED_GROUP_ID)
    if not is_member:
        invite_link ="https://t.me/+K2De7eeAtZI2NDNi"   # guruh uchun invite link yoki username
        await message.answer(f"❗️Botdan foydalanish uchun quyidagi guruhga a'zo bo'lishingiz kerak:\n👉 {invite_link}")
        return

    
    if is_user_registered(telegram_id):
        # await message.answer("✅ Siz allaqachon ro'yxatdan o'tgansiz.", reply_markup=ReplyKeyboardRemove())
        await message.answer("Xizmat turini tanlang 👇",reply_markup= await kb.get_main_keyboard())

    else:
        await message.answer("Ro'yxatdan o'tish uchun telefon raqamingizni yuboring 👇", reply_markup= await kb.get_phone_keyboard())



@router.message(lambda message: message.contact is not None)
async def handler_contact(message: Message):
    contact = message.contact
    telegram_id = message.from_user.id

    if contact.user_id != telegram_id:
        await message.answer("❌ Iltimos, faqat o'z telefon raqamingizni yuboring.")
        return
    
    phone = contact.phone_number
    if not phone.startswith('+'):
        phone = "+" + phone

    full_name = f"{message.from_user.full_name}"

    if is_user_registered(telegram_id):
        await message.answer("🔁 Siz allaqachon ro'yxatdan o'tgansiz.", reply_markup=ReplyKeyboardRemove())
    else:
        register_user(telegram_id, full_name, phone)
        await message.answer(f"✅ Ro'yxatdan muvaffaqiyatli o'tdingiz!\n📞 Telefon: {phone}", reply_markup= await kb.get_main_keyboard())



# @router.message(Command('start'))
# async def start_command(message: Message):#,roles: list[str]
#     # await message.answer(f"Sizning Telegram ID: {message.from_user.id}")
#     await message.answer(f"Hush kelibsiz, {message.from_user.full_name}!", reply_markup=await kb.get_main_keyboard())




@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

@router.message(F.text == "Orqaga")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




   







    