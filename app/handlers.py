import os
import tempfile
import pandas as pd
from aiogram import Router, F
from aiogram.types import Message, InputFile, ReplyKeyboardRemove
from aiogram.filters import Command
from app.keyboards import get_main_keyboard, otz_keyboard, region_keyboard
from app.otz import check_lavozim

router = Router()

# Define regions dynamically (consider fetching from a config or database)
REGIONS = ['Jami', 'Asaka', 'Toshkent', 'Xorazm']
TOSHKENT_BRANCHES = ['Toshkent(ofis)', 'Toshkent(SKD)']

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hush kelibsiz. Quyidagi xizmatlardan birini tanlang",
                        reply_markup=await get_main_keyboard())

@router.message(F.text == "Chiqish")
async def exit_command(message: Message):
    await message.answer("Xayr, yana kutib qolamiz", reply_markup=ReplyKeyboardRemove())

@router.message(F.text == "Orqaga")
async def back_command(message: Message):
    await message.answer("Siz asosiy menudasiz.", reply_markup=await get_main_keyboard())

@router.message(F.text == "OTZ")
async def otz_command(message: Message):
    await message.answer("Quyidagilardan birini tanlang!", reply_markup=await otz_keyboard())

@router.message(F.text == "Lavozim")
async def lavozim_command(message: Message):
    await message.answer("Quyidagilardan birini tanlang: ", reply_markup=await region_keyboard())

@router.message(F.text.in_(REGIONS))
async def filter_byregion(message: Message):
    try:
        # Fetch data
        res = await check_lavozim()
        if not res or len(res) < 2:
            await message.answer("Xatolik: Ma'lumotlar yuklanmadi.")
            return
        borlar, yoqlar = res
        if not isinstance(borlar, pd.DataFrame) or not isinstance(yoqlar, pd.DataFrame):
            await message.answer("Xatolik: Ma'lumotlar formati noto'g'ri.")
            return

        # Calculate total counts
        borcount = len(borlar)
        yoqcount = len(yoqlar)
        jami = borcount + yoqcount

        # Create temporary file
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            file_path = tmp.name

        # Filter by region
        if message.text == "Jami":
            bor = borlar
            yoq = yoqlar
        elif message.text == "Asaka":
            bor = borlar[borlar['branchName'] == "Asaka"]
            yoq = yoqlar[yoqlar['branchName'] == "Asaka"]
        elif message.text == "Xorazm":
            bor = borlar[borlar['branchName'] == "Xorazm"]
            yoq = yoqlar[yoqlar['branchName'] == "Xorazm"]
        elif message.text == "Toshkent":
            bor = borlar[borlar['branchName'].isin(TOSHKENT_BRANCHES)]
            yoq = yoqlar[yoqlar['branchName'].isin(TOSHKENT_BRANCHES)]
        else:
            await message.answer("Noma'lum region tanlandi.")
            return

        # Calculate filtered counts
        bor_count = len(bor)
        yoq_count = len(yoq)
        jami_count = bor_count + yoq_count

        # Send summary
        await message.answer(
            f"{message.text} bo'yicha ma'lumot: \n"
            f"Jami: {jami_count} \n"
            f"Borlar: {bor_count} \n"
            f"Yo'qlar: {yoq_count}"
        )

        # Save to Excel
        if bor_count == 0 and yoq_count == 0:
            await message.answer("Ma'lumotlar topilmadi.")
            os.remove(file_path)
            return

        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            bor.to_excel(writer, sheet_name="Borlar", index=False)
            yoq.to_excel(writer, sheet_name="Yoqlar", index=False)

        # Send Excel file
        await message.answer("Fayl tayyorlanmoqda...")
        await message.answer_document(
            InputFile(file_path),
            caption="Ma'lumotlar 'filtered_data.xlsx' fayliga saqlandi."
        )

        # Clean up
        os.remove(file_path)

    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {str(e)}")

# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InputFile
# from aiogram.filters import CommandStart, Command
# import app.keyboards as kb
# from app.otz import check_lavozim
# from app.getData import GetHRP
# import requests
# import pandas as pd
# import os

# router = Router()


# @router.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer("Hush kelibsiz. Quyidagi xizmatlardan birini tanlang", reply_markup= await kb.get_main_keyboard())


# @router.message(F.text == "Chiqish")
# async def exit_command(message: Message):
#     await message.answer("Xayr, yana kutib qolamiz", reply_markup= ReplyKeyboardRemove())
    
    

# @router.message(F.text == "Orqaga")
# async def back_command(message: Message):
#     await message.answer("Siz asosiy menudasiz.", reply_markup= await kb.get_main_keyboard())




# @router.message(F.text == "OTZ")
# async def otz_command(message: Message):
#     await message.answer("Quyidagilardan birini tanlang!", reply_markup= await kb.otz_keyboard())


# @router.message(F.text == 'Lavozim')

# async def lavozim_command(message: Message):
#     await message.answer("Quyidagilardan birini tanlang: ", reply_markup= await kb.region_keyboard())

# regions = ['Jami', 'Asaka', 'Toshkent', 'Xorazm']

# @router.message(F.text.in_(regions))
# async def filter_byregion(message: Message):
#     res = await check_lavozim()
#     borlar = res[0]
#     yoqlar = res[1]
#     borcount = len(borlar)
#     yoqcount = len(yoqlar)
#     jami = borcount+yoqcount
#     if message.text == "Jami":
#         await message.answer(f"Lavozim yo'riqnomalar bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {borcount} \n Yo'qlar: {yoqcount} ")
#         with pd.ExcelWriter('filtered_data.xlsx') as writer:
#             borlar.to_excel(writer, sheet_name='Borlar', index=False)
#             yoqlar.to_excel(writer, sheet_name='Yoqlar', index=False)
       
#        # Send the Excel file as a document
#         await message.answer_document(InputFile(path='filtered_data.xlsx'), caption="Ma'lumotlar 'filtered_data.xlsx' fayliga saqlandi.")

#     elif message.text == "Asaka":
#         bor = borlar[borlar['branchName'] == "Asaka"]
#         yoq = yoqlar[yoqlar['branchName'] == "Asaka"]
        
#         bor_count = len(bor)
#         yoq_count = len(yoq)
#         jami = bor_count + yoq_count
#         await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
#         # Save the filtered data to an Excel file
#         with pd.ExcelWriter('filtered_data.xlsx') as writer:
#             bor.to_excel(writer, sheet_name='Borlar', index=False)
#             yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
#         # Send the Excel file as a document
#         await message.answer_document(InputFile(path='filtered_data.xlsx'), caption="Ma'lumotlar 'filtered_data.xlsx' fayliga saqlandi.")


#     elif message.text == "Xorazm":
#         bor = borlar[borlar['branchName'] == "Xorazm"]
#         yoq = yoqlar[yoqlar['branchName'] == "Xorazm"]
        
#         bor_count = len(bor)
#         yoq_count = len(yoq)
#         jami = bor_count + yoq_count
#         await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
    
#         with pd.ExcelWriter('filtered_data.xlsx') as writer:
#             bor.to_excel(writer, sheet_name='Borlar', index=False)
#             yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
#         # Send the Excel file as a document
#         await message.answer_document(InputFile(path='filtered_data.xlsx'), caption="Ma'lumotlar 'filtered_data.xlsx' fayliga saqlandi.")

#     elif message.text == "Toshkent":
#         bor = borlar[(borlar['branchName'] == "Toshkent(ofis)") | (borlar['branchName'] == "Toshkent(SKD)")]
#         yoq = yoqlar[(yoqlar['branchName'] == "Toshkent(ofis)") | (yoqlar['branchName'] == "Toshkent(SKD)")]
        
#         bor_count = len(bor)
#         yoq_count = len(yoq)
#         jami = bor_count + yoq_count
#         await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")

#         with pd.ExcelWriter('filtered_data.xlsx') as writer:
#             bor.to_excel(writer, sheet_name='Borlar', index=False)
#             yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
#         # Send the Excel file as a document

#         await message.answer_document(InputFile(path='filtered_data.xlsx'), caption="Ma'lumotlar 'filtered_data.xlsx' fayliga saqlandi.")
            
#     else:
#         await message.answer(message.text)
    
    # 


















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