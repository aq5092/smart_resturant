from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton



async def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text="OTZ"), KeyboardButton(text="Kadr")],
            [KeyboardButton(text="Kasaba ko'mitasi"), KeyboardButton(text="OTHER")],
            [KeyboardButton(text="Chiqish")]
        ],
        resize_keyboard=True
    )

async def otz_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Lavozim"), KeyboardButton(text="Nizom")],
            [KeyboardButton(text="Boshqalar"), KeyboardButton(text="Orqara")]
        ],
        resize_keyboard=True
        ##, one_time_keyboard=True
    )