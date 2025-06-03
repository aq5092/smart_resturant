from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from otz.lavozimlar import check_lavozim
from app.getData import GetHRP
# from app.db import init_db, is_user_registered, register_user

import requests
import pandas as pd
import os

router = Router()

@router.message(Command('start'))
async def start_command(message: Message, role: str):
    await message.answer(f"Sizning Telegram ID: {message.from_user.id}")
    await message.answer(f"Hush kelibsiz, {role}!", reply_markup=await kb.get_main_keyboard())


@router.message(Command('admin'))
async def admin_command(message: Message, role: str):
    if role == 'admin':
        await message.answer("Admin panelga xush kelibsiz!", reply_markup=await kb.get_main_keyboard())
    else:
        await message.answer("Kechirasiz, bu bo'lim faqat adminlar uchun", reply_markup=ReplyKeyboardRemove())

# @router.message(CommandStart())
# async def start_command(message: Message):
#     telegram_id = message.from_user.id
#     if is_user_registered(telegram_id):
#         await message.answer("Xizmat turini tanlang", reply_markup=await kb.get_main_keyboard())

#     else:
#         await message.answer("Ro'hatdan o'tish uchun Userni kiriting")
#         await message.answer("Passwordni kiriting")
#         await message.answer("Telefon raqamingizni yoboring", reply_markup= await kb.get_phone_keyboard())



# @router.message(lambda message:message.contact is not None)
# async def handler_contact(message:Message):
#     contact = message.contact
#     telegram_id = message.from_user.id
#     if contact.user_id != telegram_id:
#         await message.answer("Iltimos faqat o'z telefon raqamingizni yuboring")
#         return
    
#     phone = contact.phone_number
#     if not phone.startswith('+'):
#         phone = "+" + phone
    
#     if is_user_registered(telegram_id):
#         await message.answer("Siz allaqazon ro'yhatdan o'tgansiz", reply_markup= ReplyKeyboardRemove())

#     else:
#         register_user(telegram_id,name, password, phone) 


# @router.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer("Hush kelibsiz. Quyidagi xizmatlardan birini tanlang", reply_markup= await kb.get_main_keyboard())



@router.message(F.text == "Bosh sahifa")
async def main_menu_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())

@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

@router.message(F.text == "Orqaga")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




# @router.message(F.text == "OTZ")
# async def otz_command(message: Message, role: str):
#     if role == "otz":
#         await message.answer("Quyidagilardan birini tanlang!", reply_markup= await kb.otz_keyboard())
#     else:
#         await message.answer("Kechirasiz, siz bundan foydalana olmaysiz.." )


# @router.message(F.text == 'Lavozim')

# async def lavozim_command(message: Message):
#     await message.answer("Quyidagilardan birini tanlang: ", reply_markup= await kb.region_keyboard())

# regions = ['Jami', 'Asaka', 'Toshkent', 'Xorazm']

# @router.message(F.text.in_(regions))
# async def filter_byregion(message: Message):
    res = await check_lavozim()
    borlar = res[0]
    yoqlar = res[1]
    borcount = len(borlar)
    yoqcount = len(yoqlar)
    jami = borcount+yoqcount
    if message.text == "Jami":
        await message.answer(f"Lavozim yo'riqnomalar bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {borcount} \n Yo'qlar: {yoqcount} ")
        with pd.ExcelWriter('lavozimlar.xlsx') as writer:
            borlar.to_excel(writer, sheet_name='Borlar', index=False)
            yoqlar.to_excel(writer, sheet_name='Yoqlar', index=False)
       
       # Send the Excel file as a document
        file_path = FSInputFile('lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    elif message.text == "Asaka":
        bor = borlar[borlar['branchName'] == "Asaka"]
        yoq = yoqlar[yoqlar['branchName'] == "Asaka"]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
        # Save the filtered data to an Excel file
        with pd.ExcelWriter('lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document
        file_path = FSInputFile('lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")


    elif message.text == "Xorazm":
        bor = borlar[borlar['branchName'] == "Xorazm"]
        yoq = yoqlar[yoqlar['branchName'] == "Xorazm"]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
    
        with pd.ExcelWriter('lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document
        file_path = FSInputFile('lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    elif message.text == "Toshkent":
        bor = borlar[(borlar['branchName'] == "Toshkent(ofis)") | (borlar['branchName'] == "Toshkent(SKD)")]
        yoq = yoqlar[(yoqlar['branchName'] == "Toshkent(ofis)") | (yoqlar['branchName'] == "Toshkent(SKD)")]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")

        with pd.ExcelWriter('lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document

        file_path = FSInputFile('lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")
            
    else:
        await message.answer(message.text)
    
    


















    # TOKEN = "4620|xDz0N9JvIiMBB7TQYQwSmqar7cbXKjTIDo9eU4ha"
    # url = "https://b-hr.uzautomotors.com/api/position-description-detail"
    
    # headers = {
    #     "Authorization": f"Bearer {TOKEN}"
    # }

    # # response = requests.get("https://b-hr.uzautomotors.com/api/test")
    # response = requests.get(url, headers=headers)

    # # print("Status:", response.status_code)
    # # print("Text:", response.text)
    # if response.headers.get("Content-Type", "").startswith("application/json"):
    #     data = response.json()
    #     if data:
    #         df_yoqlar = pd.DataFrame(data['not_exist_position_description'])
    #         df_borlar = pd.DataFrame(data['exist_position_description'])
    #         jami = len(df_borlar)+ len(df_yoqlar)
    #         # Summarize the DataFrames to avoid long messages
    #         borlar_count = len(df_borlar)
    #         yoqlar_count = len(df_yoqlar)
    #         await message.answer(
    #             f"Lavozim yo'riqnomalar bo'yicha ma'lumotlar:\n"
    #             f"Jami: {jami}\n"
    #             f"Borlari soni: {borlar_count}\n"
    #             f"Yo'qlari soni: {yoqlar_count}"
    #         )
    #     else:
    #         await message.answer("JSON ma'lumotlar topilmadi.")
    # else:
    #     print("JSON emas:", response.text)
    #