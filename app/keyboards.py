from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton

async def get_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]],
        resize_keyboard=True,
        # one_time_keyboard=True
    )


async def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text="MMB"), KeyboardButton(text="Kadr")],
            [KeyboardButton(text="Kasaba qo'mitasi"), KeyboardButton(text="OTHER")],
            [KeyboardButton(text="Chiqish")]
        ],
        resize_keyboard=True
    )

async def otz_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Lavozim"), KeyboardButton(text="Nizom")],
            [KeyboardButton(text="Lavozim takror"), KeyboardButton(text="Kod prof")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
        ##, one_time_keyboard=True
    )


async def kadr_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="RP"), KeyboardButton(text="Report")],
            [KeyboardButton(text="Check"), KeyboardButton(text="Orqaga")]
            
        ], resize_keyboard=True
    )


async def check_rp():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Tabel bo'yicha"), KeyboardButton(text="Lavozim bo'yicha")],
            [KeyboardButton(text="Pesonal turi bo'yicha"), KeyboardButton(text="Kod bo'yicha")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
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