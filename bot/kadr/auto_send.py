import aiohttp
import pandas as pd
import io
from aiogram.types import FSInputFile
from app.get_data import get_Data

# from app.db import init_db, is_user_registered, register_user
# import logging
from aiogram import Bot


CHAT_ID = 2112762237

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKqyUbbN5yOb5-YoI0KJ7R7NF1h6sSZ5VZgKhQFjYiqZgGVJVRhU8XJTZugo7vzNhABu6KpvTkhABV/pub?gid=854712723&single=true&output=csv"


# Loggerni sozlash
# logging.basicConfig(level=logging.INFO)

# async def send_daily_tabel(bot:Bot):
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(csv_url) as resp:
#                 if resp.status == 200:
#                     csv_data = await resp.text()
                   
                   
#                     df = pd.read_csv(io.StringIO(csv_data))
#                     ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
#                     online = df[ustunlar]
#                     online = online[online['Tabel'].notna()]
#                     online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
#                     online['sh6'] = online['sh6'].fillna(0).astype(int)
#                     # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
#                     online_temp = online.rename(columns={
#                         "Kod": "department_code",
#                         "Tabel": "tabel",
#                         "profkod": "position_code",
#                         "sh6": "personal_type_id"
#                     })
                    
#                     data = await get_Data("rp-data-api")
#                     hr = pd.DataFrame(data)
#                     hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

#                     hr = hr[hrustunlar]
#                     hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
#                     merged = online_temp.merge(hr, on=["tabel"], how='left', indicator=True)
#                     # faqat online'da bo'lganlarini tanlaymiz
#                     antijoin = merged[merged['_merge'] == 'left_only']
#                     with pd.ExcelWriter('kadr/tabel_boyicha_tekshiruv.xlsx') as writer:
#                         antijoin.to_excel(writer, sheet_name='rp', index=False)
#                         # online.to_excel(writer, sheet_name='online', index=False)
                    
#                     file_path = FSInputFile('kadr/tabel_boyicha_tekshiruv.xlsx')
#                     await bot.send_document(chat_id=CHAT_ID, document=file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
#                 else:
#                     print("send_daily_tabel() da xatolik bor ")
                   
#     except Exception as e:
        
#         print(f"Xatolik: {e}")


# async def send_daily_personalturi(bot:Bot):
#     try:
#          async with aiohttp.ClientSession() as session:
#             async with session.get(csv_url) as resp:
#                 if resp.status == 200:
#                     csv_data = await resp.text()
                   
                   
#                     df = pd.read_csv(io.StringIO(csv_data))
#                     ustunlar = ["Kod", "Tabel", "profkod", "sh6"]
#                     online = df[ustunlar]
#                     online = online[online['Tabel'].notna()]
#                     online['Tabel'] = online['Tabel'].astype(str).str.zfill(4)
#                     online['sh6'] = online['sh6'].fillna(0).astype(int)
#                     # ustunlar nomlarini moslashtirib, ikkala DF'da bir xil nomli ustunlar bilan vaqtincha yangi DF yaratamiz
#                     online_temp = online.rename(columns={
#                         "Kod": "department_code",
#                         "Tabel": "tabel",
#                         "profkod": "position_code",
#                         "sh6": "personal_type_id"
#                     })
                    
#                     data = await get_Data("rp-data-api")
#                     hr = pd.DataFrame(data)
#                     hrustunlar = ["department_code","tabel","position_code","personal_type_id",]

#                     hr = hr[hrustunlar]
#                     hr['department_code'] = hr['department_code'].astype(str).str.zfill(4).str[-4:]
#                     merged = online_temp.merge(hr, on=["tabel",'personal_type_id'], how='left', indicator=True)
#                     # faqat online'da bo'lganlarini tanlaymiz
#                     antijoin = merged[merged['_merge'] == 'left_only']
#                     with pd.ExcelWriter('kadr/personal_turi_tekshiruv.xlsx') as writer:
#                         antijoin.to_excel(writer, sheet_name='rp', index=False)
#                         # online.to_excel(writer, sheet_name='online', index=False)
                    
#                     file_path = FSInputFile('kadr/personal_turi_tekshiruv.xlsx')
#                     await bot.send_document(chat_id=CHAT_ID, document=file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
#                 else:
#                     await bot.send_message(chat_id=1061444753, text="❌ Ma'lumotlarni olishda xatolik yuz berdi.")
#     except Exception as e:
#         print(f"Xatolik: {e}")


async def send_daily_kadr(bot:Bot):
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
                   
                    personalturi = online_temp.merge(hr, on=["tabel",'personal_type_id'], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    personal = personalturi[personalturi['_merge'] == 'left_only']
                   
                   ## tabel bo'yicha
                    mergedtabel = online_temp.merge(hr, on=["tabel"], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    tabel = mergedtabel[mergedtabel['_merge'] == 'left_only']
                   
                    ## lavozim bo'yicha    
                    mergedlavozim = online_temp.merge(hr, on=["tabel",'position_code'], how='left', indicator=True)
                    # faqat online'da bo'lganlarini tanlaymiz
                    lavozim = mergedlavozim[mergedlavozim['_merge'] == 'left_only']






                    with pd.ExcelWriter('kadr/kunlik_tekshiruv.xlsx') as writer:
                        tabel.to_excel(writer, sheet_name='tabel', index=False)
                        personal.to_excel(writer, sheet_name='personal turi', index=False)
                        lavozim.to_excel(writer, sheet_name='lavozim', index=False)
                        # online.to_excel(writer, sheet_name='online', index=False)
                    
                    file_path = FSInputFile('kadr/kunlik_tekshiruv.xlsx')
                    await bot.send_document(chat_id=CHAT_ID, document=file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
                else:
                    await bot.send_message(chat_id=1061444753, text="❌ Ma'lumotlarni olishda xatolik yuz berdi.")
    except Exception as e:
        print(f"Xatolik: {e}")