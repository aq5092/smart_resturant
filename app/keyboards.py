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
            [KeyboardButton(text="Lavozim takror"), KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
        ##, one_time_keyboard=True
    )


async def kadr_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="RP"), KeyboardButton(text="Report")],
            [KeyboardButton(text="Boshqalar"), KeyboardButton(text="Orqaga")]
            
        ], resize_keyboard=True
    )






async def region_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Jami"), KeyboardButton(text="Asaka")],
            [KeyboardButton(text="Toshkent"), KeyboardButton(text="Xorazm")],
            [KeyboardButton(text="Orqaga")]
        ], resize_keyboard= True
    )

async def get_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]],
        resize_keyboard= True
    )