from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import keyboards as kb
import pandas as pd
from dotenv import load_dotenv
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
load_dotenv()
import os
import re
import aiohttp


router = Router()

baseurl = os.getenv("BASE_URL")
GROUP_INVITE_LINK = os.getenv("GROUP_INVITE_LINK")
GROUP_ID = int(os.getenv("GROUP_CHAT_ID"))




async def is_user_in_group(bot, user_id: int, group_id: int) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=group_id, user_id=user_id)
        return member.status in ["member", "creator", "administrator"]
    except TelegramBadRequest:
        return False




def normalise_phone(phone: str) -> str:
    return re.sub(r"\D", "", phone.lstrip("+"))

async def register_user_to_backend(message: Message):
    payload = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username or "None",
        "first_name": message.from_user.first_name or "",
        "last_name": message.from_user.last_name or "",
        "phone": message.contact.phone_number,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(baseurl +"botusers/", json=payload) as resp:
            if resp.status in (200, 201):
                return True, await resp.json()
            else:
                text = await resp.text()
                try:
                    error = (await resp.json()).get("detail", text)
                except:
                    error = text
                return False, error

async def check_user_in_backend(message:Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(baseurl + "botusers/") as resp:
            if resp.status in (200, 201):
                data = await resp.json()
                telegram_id = message.from_user.id
                # `data` might be a list of user dicts, a list of ids, or a paginated dict
                if isinstance(data, list):
                    found = any(
                        (isinstance(item, dict) and item.get("telegram_id") == telegram_id) or (item == telegram_id)
                        for item in data
                    )
                    return bool(found)
                if isinstance(data, dict):
                    # handle paginated responses or containers with results
                    candidates = data.get("results") or data.get("data") or data.get("items")
                    if isinstance(candidates, list):
                        found = any(
                            (isinstance(item, dict) and item.get("telegram_id") == telegram_id) or (item == telegram_id)
                            for item in candidates
                        )
                        return bool(found)
                # fallback: not found
                return False
            return False


# /start buyrug‘i
@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    await message.answer("Botga xush kelibsiz!, Botdan foydalanish uchun quyidagi ko'rsatmalarga amal qiling.")

    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=await kb.get_phone_keyboard()
    )

@router.message(Command("id"))
async def get_chat_id(message: Message):
    chat = message.chat
    real_id = chat.id                     # Bu to'liq ID (superguruh bo'lsa -100...)
    
    await message.reply(
        f"👥 Guruh / Kanal ID: <code>{real_id}</code>\n"
        f"🔢 Oddiy ID: <code>{chat.id}</code>\n"
        f"📛 Nomi: {chat.title}\n"
        f"🔗 Username: @{chat.username if chat.username else 'yo‘q'}",
        parse_mode="HTML")

# Kontakt kelganda
@router.message(F.contact)
async def handle_phone(message: Message, bot: Bot):
    if not message.contact:
        return

    check_user = await check_user_in_backend(message)
    if check_user:
        await message.answer(
                "Siz oldin ro'yxatdan o'tgansiz! Botdan foydalanishingiz mumkin.",
                reply_markup=await kb.get_main_keyboard()
            )
    else:
        success, result = await register_user_to_backend(message)

        if success:
            

            await message.answer(
                f"Tabriklaymiz! Ro'yxatdan muvaffaqiyatli o'tdingiz!\n"
                f"Ismingiz: {message.from_user.first_name}",
                reply_markup=ReplyKeyboardRemove()
            )

            # Guruhga a'zo ekanligini tekshirish
            try:
                member = await bot.get_chat_member(GROUP_ID, message.from_user.id)
                if member.status in ("member", "administrator", "creator"):
                    await message.answer(
                        "Siz allaqachon guruh a'zosisiz! Botdan foydalanishingiz mumkin.",
                        reply_markup=await kb.main_keyboard()
                    )
                else:
                    await message.answer(f"Guruhga a'zo bo‘ling:\n{GROUP_INVITE_LINK}")
            except:
                await message.answer("Guruhni tekshirishda xatolik. Keyinroq urinib ko‘ring.")

        else:
            error_msg = result.get("detail") if isinstance(result, dict) else str(result)


            if "allaqachon" in error_msg.lower():
                await message.answer(
                    "Siz oldin ro'yxatdan o'tgansiz! Botdan foydalanishingiz mumkin.",
                    reply_markup=await kb.main_keyboard()
                )
            else:
                await message.answer(f"Xatolik: {error_msg}")


@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

@router.message(F.text == "Orqaga")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




   







    