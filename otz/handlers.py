from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from otz.lavozimlar import check_lavozim
from app.getData import GetHRP
from otz.duplicates import check_duplicates
# from app.db import init_db, is_user_registered, register_user

import pandas as pd


otzrouter = Router()

@otzrouter.message(F.text == "OTZ")
async def otz_command(message: Message, role: str):
    if role == "otz":
        await message.answer("Quyidagilardan birini tanlang!", reply_markup= await kb.otz_keyboard())
    else:
        await message.answer("Kechirasiz, siz bundan foydalana olmaysiz.." )


@otzrouter.message(F.text == 'Lavozim')

async def lavozim_command(message: Message):
    await message.answer("Quyidagilardan birini tanlang: ", reply_markup= await kb.region_keyboard())

regions = ['Jami', 'Asaka', 'Toshkent', 'Xorazm']

@otzrouter.message(F.text.in_(regions))
async def filter_byregion(message: Message):
    res = await check_lavozim()
    borlar = res[0]
    yoqlar = res[1]
    borcount = len(borlar)
    yoqcount = len(yoqlar)
    jami = borcount+yoqcount
    if message.text == "Jami":
        await message.answer(f"Lavozim yo'riqnomalar bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {borcount} \n Yo'qlar: {yoqcount} ")
        with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
            borlar.to_excel(writer, sheet_name='Borlar', index=False)
            yoqlar.to_excel(writer, sheet_name='Yoqlar', index=False)
       
       # Send the Excel file as a document
        file_path = FSInputFile('otz/lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    elif message.text == "Asaka":
        bor = borlar[borlar['branchName'] == "Asaka"]
        yoq = yoqlar[yoqlar['branchName'] == "Asaka"]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
        # Save the filtered data to an Excel file
        with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document
        file_path = FSInputFile('otz/lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")


    elif message.text == "Xorazm":
        bor = borlar[borlar['branchName'] == "Xorazm"]
        yoq = yoqlar[yoqlar['branchName'] == "Xorazm"]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
    
        with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document
        file_path = FSInputFile('otz/lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    elif message.text == "Toshkent":
        bor = borlar[(borlar['branchName'] == "Toshkent(ofis)") | (borlar['branchName'] == "Toshkent(SKD)")]
        yoq = yoqlar[(yoqlar['branchName'] == "Toshkent(ofis)") | (yoqlar['branchName'] == "Toshkent(SKD)")]
        
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami = bor_count + yoq_count
        await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")

        with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
            bor.to_excel(writer, sheet_name='Borlar', index=False)
            yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
        # Send the Excel file as a document

        file_path = FSInputFile('otz/lavozimlar.xlsx')
        await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")
            
    else:
        await message.answer(message.text)
    
    

@otzrouter.message(F.text == 'Lavozim takror')
async def filter_byduplicates(message: Message):
    res = await check_duplicates()
    # ['code3', 'code3_name', 'branchName', 'depName', 'depCode', 'profName', 'profCode', 'rate_count', 'rate_count_bp', 'dublicate_count']
    # cols = res.columns.tolist()
    group = res.groupby('branchName')['dublicate_count'].sum()

    with pd.ExcelWriter("otz/duplicates.xlsx") as writer:
        group.to_excel(writer, sheet_name="duplicate")
    
    file_path = FSInputFile('otz/duplicates.xlsx')
    await message.answer_document(file_path, caption="Ma'lumotlar duplicates.xlsx fayliga saqlandi")
    # print(group)
    # await message.answer("Biz lavozim duplicates ni ketshirmoqdamiz")
    # await message.answer(f"Regionlar bo'yicha \n {group}")
















    