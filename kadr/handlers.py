from aiogram import Router, F
from aiogram.types import Message, FSInputFile, InputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from app.get_data import get_Data
from kadr.kadrdb import get_hreport
import pandas as pd
import aiohttp
import io

kadrrouter = Router()

@kadrrouter.message(F.text == "Kadr")
async def kadr_command(message: Message, roles: list[str]):
    if "kadr" in roles:
        await message.answer("Quyidagilardan birini tanlang!", reply_markup=await kb.kadr_keyboard())
    else:
        await message.answer("Kechirasiz, siz bundan foydalana olmaysiz..")


@kadrrouter.message(F.text == "Report")
async def report_command(message: Message):
    # df = await get_hreport()
    # col = df.columns.tolist()
    await message.answer(text="Tahlil qilinmoqda")


csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKqyUbbN5yOb5-YoI0KJ7R7NF1h6sSZ5VZgKhQFjYiqZgGVJVRhU8XJTZugo7vzNhABu6KpvTkhABV/pub?gid=854712723&single=true&output=csv"





@kadrrouter.message(F.text == "Check")
async def check_command(message:Message):
    await message.answer(text="Quyidagilardan birini tanlang", reply_markup= await kb.check_rp())

@kadrrouter.message(F.text == "Tabel bo'yicha")
async def check_command(message: Message):
    
    await message.answer("⏳ Ma'lumotlar olinmoqda...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(csv_url) as resp:
                if resp.status == 200:
                    csv_data = await resp.text()
                   
                   
                    df = pd.read_csv(io.StringIO(csv_data))
                    ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
                    online = df[ustunlar]
                    online = online[online['Tabel'].notna()]
                    online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
                    online['sh6'] = online['sh6'].fillna(0).astype(int)
                    # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
                    online_temp = online.rename(columns={
                        "Kod": "department_code",
                        "Tabel": "tabel",
                        "profkod": "position_code",
                        "sh6": "personal_type_id"
                    })
                    
                    data = await get_Data("rp-data-api")
                    hr = pd.DataFrame(data)
                    hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

                    hr = hr[hrustunlar]
                    hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
                    merged = online_temp.merge(hr, on=["tabel"], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    antijoin = merged[merged['_merge'] == 'left_only']
                    with pd.ExcelWriter('kadr/rp.xlsx') as writer:
                        antijoin.to_excel(writer, sheet_name='rp', index=False)
                        # online.to_excel(writer, sheet_name='online', index=False)
                    
                    file_path = FSInputFile('kadr/rp.xlsx')
                    await message.answer_document(file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
                else:
                    await message.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")
    except Exception as e:
        await message.answer(f"⚠️ Xatolik: {e}")



@kadrrouter.message(F.text == "Lavozim bo'yicha")
async def check_command(message: Message):
    
    await message.answer("⏳ Ma'lumotlar olinmoqda...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(csv_url) as resp:
                if resp.status == 200:
                    csv_data = await resp.text()
                   
                   
                    df = pd.read_csv(io.StringIO(csv_data))
                    ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
                    online = df[ustunlar]
                    online = online[online['Tabel'].notna()]
                    online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
                    online['sh6'] = online['sh6'].fillna(0).astype(int)
                    # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
                    online_temp = online.rename(columns={
                        "Kod": "department_code",
                        "Tabel": "tabel",
                        "profkod": "position_code",
                        "sh6": "personal_type_id"
                    })
                    
                    data = await get_Data("rp-data-api")
                    hr = pd.DataFrame(data)
                    hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

                    hr = hr[hrustunlar]
                    hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
                    merged = online_temp.merge(hr, on=["tabel",'position_code'], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    antijoin = merged[merged['_merge'] == 'left_only']
                    with pd.ExcelWriter('kadr/rp.xlsx') as writer:
                        antijoin.to_excel(writer, sheet_name='rp', index=False)
                        # online.to_excel(writer, sheet_name='online', index=False)
                    
                    file_path = FSInputFile('kadr/rp.xlsx')
                    await message.answer_document(file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
                else:
                    await message.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")
    except Exception as e:
        await message.answer(f"⚠️ Xatolik: {e}")                   


@kadrrouter.message(F.text == "Pesonal turi bo'yicha")
async def check_command(message: Message):
    
    await message.answer("⏳ Ma'lumotlar olinmoqda...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(csv_url) as resp:
                if resp.status == 200:
                    csv_data = await resp.text()
                   
                   
                    df = pd.read_csv(io.StringIO(csv_data))
                    ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
                    online = df[ustunlar]
                    online = online[online['Tabel'].notna()]
                    online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
                    online['sh6'] = online['sh6'].fillna(0).astype(int)
                    # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
                    online_temp = online.rename(columns={
                        "Kod": "department_code",
                        "Tabel": "tabel",
                        "profkod": "position_code",
                        "sh6": "personal_type_id"
                    })
                    
                    data = await get_Data("rp-data-api")
                    hr = pd.DataFrame(data)
                    hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

                    hr = hr[hrustunlar]
                    hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
                    merged = online_temp.merge(hr, on=["tabel",'personal_type_id'], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    antijoin = merged[merged['_merge'] == 'left_only']
                    with pd.ExcelWriter('kadr/rp.xlsx') as writer:
                        antijoin.to_excel(writer, sheet_name='rp', index=False)
                        # online.to_excel(writer, sheet_name='online', index=False)
                    
                    file_path = FSInputFile('kadr/rp.xlsx')
                    await message.answer_document(file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
                else:
                    await message.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")
    except Exception as e:
        await message.answer(f"⚠️ Xatolik: {e}")                   


@kadrrouter.message(F.text == "Kod bo'yicha")
async def check_command(message: Message):
    
    await message.answer("🛠️ Bu xizmat hali tayyor emas...")
    # await message.answer("⏳ Ma'lumotlar olinmoqda...")
    # try:
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(csv_url) as resp:
    #             if resp.status == 200:
    #                 csv_data = await resp.text()
                   
                   
    #                 df = pd.read_csv(io.StringIO(csv_data))
    #                 ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
    #                 online = df[ustunlar]
    #                 online = online[online['Tabel'].notna()]
    #                 online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
    #                 online['sh6'] = online['sh6'].fillna(0).astype(int)
    #                 # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
    #                 online_temp = online.rename(columns={
    #                     "Kod": "department_code",
    #                     "Tabel": "tabel",
    #                     "profkod": "position_code",
    #                     "sh6": "personal_type_id"
    #                 })
                    
    #                 data = await get_Data("rp-data-api")
    #                 hr = pd.DataFrame(data)
    #                 hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

    #                 hr = hr[hrustunlar]
    #                 hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
    #                 print('online', online_temp.dtypes())
    #                 print('hr', hr.dtypes())

    #                 # merged = online_temp.merge(hr, on=["tabel",'department_code'], how='left', indicator=True)
                    
                    
    #                 # faqat online'da bo'lganlarini tanlaymiz
                    
                    
                    
    #                 # antijoin = merged[merged['_merge'] == 'left_only']

    #                 # with pd.ExcelWriter('kadr/rp.xlsx') as writer:
    #                 #     antijoin.to_excel(writer, sheet_name='rp', index=False)
    #                 #     # online.to_excel(writer, sheet_name='online', index=False)
                    
    #                 # file_path = FSInputFile('kadr/rp.xlsx')
    #                 # await message.answer_document(file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
    #             else:
    #                 await message.answer("❌ Ma'lumotlarni olishda xatolik yuz berdi.")
    # except Exception as e:
    #     await message.answer(f"⚠️ Xatolik: {e}")     

    # if df is not None:
    #     with pd.ExcelWriter('kadr/report.xlsx') as writer:
    #         df.to_excel(writer, sheet_name='Report', index=False)
        
    #     # Send the Excel file as a document
    #     file_path = FSInputFile('kadr/report.xlsx')
    #     await message.answer_document(file_path, caption="Ma'lumotlar 'report.xlsx' fayliga saqlandi.")
    # else:
    #     await message.answer("Ma'lumot topilmadi.")