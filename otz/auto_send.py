import pandas as pd
from aiogram.types import FSInputFile
from app.get_data import get_Data

from aiogram import Bot
CHAT_ID = 306794063 # Botirjon
async def send_daily_mmb(bot:Bot):

    try:
        data = await get_Data("position-description-detail")
        if data:
            
            df_yoqlar = pd.DataFrame(data['not_exist_position_description'])
             
            df_yoqlar = df_yoqlar[df_yoqlar['branchName'] == 'Asaka']
            df_borlar = pd.DataFrame(data['exist_position_description'])
            df_borlar = df_borlar[df_borlar['branchName'] == 'Asaka']

            jami = len(df_borlar)+ len(df_yoqlar)
            # Summarize the DataFrames to avoid long messages
            borlar_count = len(df_borlar)
            yoqlar_count = len(df_yoqlar)
            # print(df_borlar.head())
            with pd.ExcelWriter('otz/kunlik_tekshiruv.xlsx') as writer:


                df_yoqlar.to_excel(writer, sheet_name='yoqlar', index=False)
                df_borlar.to_excel(writer, sheet_name='borlar', index=False)
                file_path = FSInputFile('otz/kunlik_tekshiruv.xlsx')
            await bot.send_message(chat_id=CHAT_ID, text="Lavozim yo'riqnomalar bo'yicha kunlik xisobot (Asaka): \n Jami: {jami} \n Borlar: {borlar_count} \n Yoqlar: {yoqlar_count}".format(jami=jami, borlar_count=borlar_count, yoqlar_count=yoqlar_count))
            await bot.send_document(chat_id=CHAT_ID, document=file_path, caption="✅ Ma'lumotlar muvaffaqiyatli olindi.")
        else:
            print('Malumot yoq')

    except Exception as e:
        print(f"Xatolik: {e}")

