from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from otz.lavozimlar import check_lavozim
from otz.nizomlar import check_nizomlar
from otz.duplicates import check_duplicates
from app.states import ReportState
from aiogram.fsm.context import FSMContext
   
# from app.db import init_db, is_user_registered, register_user

import pandas as pd

regions = ['Jami', 'Asaka', 'Toshkent', 'Xorazm']

otzrouter = Router()

@otzrouter.message(F.text == "MMB")
async def otz_command(message: Message,  roles: list[str]):
    if "otz" in roles:
        await message.answer("Quyidagilardan birini tanlang!", reply_markup= await kb.otz_keyboard())
    else:
        await message.answer("Kechirasiz, siz bundan foydalana olmaysiz.." )



# === LAVOZIM ===
@otzrouter.message(F.text == 'Lavozim')
async def lavozim_start(message: Message, state: FSMContext):
    await state.set_state(ReportState.lavozim)
    await message.answer("Qaysi hudud bo‘yicha ma'lumot kerak?", reply_markup=await kb.region_keyboard())



@otzrouter.message(ReportState.lavozim)
async def lavozim_region_handler(message: Message, state: FSMContext):
    res = await check_lavozim()
    borlar, yoqlar = res[0], res[1]
    if message.text == "Toshkent":
        bor = borlar[borlar['branchName'].isin(["Toshkent(ofis)", "Toshkent(SKD)"])]
        yoq = yoqlar[yoqlar['branchName'].isin(["Toshkent(ofis)", "Toshkent(SKD)"])]
    elif message.text in ["Asaka", "Xorazm"]:
        bor = borlar[borlar['branchName'] == message.text]
        yoq = yoqlar[yoqlar['branchName'] == message.text]
    elif message.text == "Jami":
        bor = borlar
        yoq = yoqlar
    else:
        await message.answer("Noto‘g‘ri tanlov.")
        return

    borcount, yoqcount = len(bor), len(yoq)
    jami = borcount + yoqcount
    await message.answer(f"{message.text} uchun lavozimlar:\nJami: {jami}\nBor: {borcount}\nYoq: {yoqcount}")

    with pd.ExcelWriter("otz/lavozimlar.xlsx") as writer:
        bor.to_excel(writer, sheet_name="Borlar", index=False)
        yoq.to_excel(writer, sheet_name="Yoqlar", index=False)

    file_path = FSInputFile("otz/lavozimlar.xlsx")

    await message.answer_document(file_path, caption="Lavozim fayliga saqlandi.")
    await state.clear()




# === NIZOM ===
@otzrouter.message(F.text == 'Nizom')
async def nizom_start(message: Message, state: FSMContext):
    await state.set_state(ReportState.nizom)
    await message.answer("Qaysi hudud bo‘yicha ma'lumot kerak?", reply_markup=await kb.region_keyboard())

@otzrouter.message(ReportState.nizom)
async def nizom_region_handler(message: Message, state: FSMContext):
    res = await check_nizomlar()
    bor, yoq = res[0], res[1]

    if message.text == "Toshkent":
        bor = bor[bor['branchName'].isin(["Toshkent(ofis)", "Toshkent(SKD)"])]
        yoq = yoq[yoq['branchName'].isin(["Toshkent(ofis)", "Toshkent(SKD)"])]
    elif message.text in ["Asaka", "Xorazm"]:
        bor = bor[bor['branchName'] == message.text]
        yoq = yoq[yoq['branchName'] == message.text]
    elif message.text == "Jami":
        pass  # bor va yoq ni to‘liq olib qo‘yamiz
    else:
        await message.answer("Noto‘g‘ri tanlov.")
        return

    borcount, yoqcount = len(bor), len(yoq)
    jami = borcount + yoqcount
    await message.answer(f"{message.text} uchun nizomlar:\nJami: {jami}\nBor: {borcount}\nYoq: {yoqcount}")

    with pd.ExcelWriter("otz/nizomlar.xlsx") as writer:
        bor.to_excel(writer, sheet_name="Bor Nizomlar", index=False)
        yoq.to_excel(writer, sheet_name="Yoq Nizomlar", index=False)

    await message.answer_document(FSInputFile("otz/nizomlar.xlsx"), caption="Nizom fayliga saqlandi.")
    await state.clear()


# === DUPLICATE ===
@otzrouter.message(F.text == "Lavozim takror")
async def takror_lavozim_start(message: Message, state: FSMContext):
    await state.set_state(ReportState.duplicate)
    await message.answer("Qaysi hudud bo'yicha ma'lumot kerak?", reply_markup= await kb.region_keyboard())

@otzrouter.message(ReportState.duplicate)
async def duplicate_region_handler(message: Message, state: FSMContext):
    res = await check_duplicates()
    if message.text == "Toshkent":
        res = res[res['branchName'].isin(["Toshkend(ofis)", "Toshkent(SKD)"])]
    elif message.text in ["Asaka", "Xorazm"]:
        res = res[res['branchName'] == message.text]
    elif message.text == "Jami":
        pass
    else:
        await message.answer("Noto'g'ri tanlov.")
        return

    await message.answer(f"Takrorlanayotgan lavozimlar soni: {len(res)}")
    with pd.ExcelWriter("otz/duplicates.xlsx") as writer:
        res.to_excel(writer, sheet_name="duplikatlar", index=False)
    await message.answer_document(FSInputFile("otz/duplicates.xlsx"), caption="Duplikatlar faylga saqlandi.")
    await state.clear()




    # borcount = len(borlar)
    # yoqcount = len(yoqlar)
    # jami = borcount+yoqcount
    # if message.text == "Jami":
    #     await message.answer(f"Lavozim yo'riqnomalar bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {borcount} \n Yo'qlar: {yoqcount} ")
    #     with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
    #         borlar.to_excel(writer, sheet_name='Borlar', index=False)
    #         yoqlar.to_excel(writer, sheet_name='Yoqlar', index=False)
       
    #    # Send the Excel file as a document
    #     file_path = FSInputFile('otz/lavozimlar.xlsx')
    #     await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    # elif message.text == "Asaka":
    #     bor = borlar[borlar['branchName'] == "Asaka"]
    #     yoq = yoqlar[yoqlar['branchName'] == "Asaka"]
        
    #     bor_count = len(bor)
    #     yoq_count = len(yoq)
    #     jami = bor_count + yoq_count
    #     await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
    #     # Save the filtered data to an Excel file
    #     with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
    #         bor.to_excel(writer, sheet_name='Borlar', index=False)
    #         yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
    #     # Send the Excel file as a document
    #     file_path = FSInputFile('otz/lavozimlar.xlsx')
    #     await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")


    # elif message.text == "Xorazm":
    #     bor = borlar[borlar['branchName'] == "Xorazm"]
    #     yoq = yoqlar[yoqlar['branchName'] == "Xorazm"]
        
    #     bor_count = len(bor)
    #     yoq_count = len(yoq)
    #     jami = bor_count + yoq_count
    #     await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")
    
    #     with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
    #         bor.to_excel(writer, sheet_name='Borlar', index=False)
    #         yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
    #     # Send the Excel file as a document
    #     file_path = FSInputFile('otz/lavozimlar.xlsx')
    #     await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")

    # elif message.text == "Toshkent":
    #     bor = borlar[(borlar['branchName'] == "Toshkent(ofis)") | (borlar['branchName'] == "Toshkent(SKD)")]
    #     yoq = yoqlar[(yoqlar['branchName'] == "Toshkent(ofis)") | (yoqlar['branchName'] == "Toshkent(SKD)")]
        
    #     bor_count = len(bor)
    #     yoq_count = len(yoq)
    #     jami = bor_count + yoq_count
    #     await message.answer(f"{message.text} bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {bor_count} \n Yo'qlar: {yoq_count} ")

    #     with pd.ExcelWriter('otz/lavozimlar.xlsx') as writer:
    #         bor.to_excel(writer, sheet_name='Borlar', index=False)
    #         yoq.to_excel(writer, sheet_name='Yoqlar', index=False)
    #     # Send the Excel file as a document

    #     file_path = FSInputFile('otz/lavozimlar.xlsx')
    #     await message.answer_document(file_path, caption="Ma'lumotlar 'lavozimlar.xlsx' fayliga saqlandi.")
            
    # else:
    #     await message.answer(message.text)
    




# @otzrouter.message(F.text == 'Nizom')
# async def nizom_command(message: Message):
#     await message.answer("Quyidagilardan birini tanlang:", reply_markup= await kb.region_keyboard())

# region = ["Jami", 'Asaka', 'Toshkent', 'Xorazm']

# @otzrouter.message(F.text == "Jami")
# async def nizom_filter(message: Message):
#     res = await check_nizomlar()
#     born = res[0]
#     yoqn = res[1]
#     borcount = len(born)
#     yoqcount = len(yoqn)
#     jami = borcount+yoqcount

#     if message.text == "Jami":
#         await message.answer(f"Bo'lim nizomlari bo'yicha ma'lumot: \n Jami: {jami} \n Borlar: {borcount} \n Yo'qlar: {yoqcount} ")
#     await message.answer("⏳ Ma'lumotlar olinmoqda...")
#     with pd.ExcelWriter('otz/nizomlar.xlsx') as writer2:
#         born.to_excel(writer2, sheet_name="bor nizomlar", index= False)
#         yoqn.to_excel(writer2, sheet_name='yoq nizomlar', index=False)
    
#     file_path = FSInputFile( "otz/nizomlar.xlsx")
#     await message.answer_document(file_path, caption="Ma'lumotlar nizomlar fayliga saqlandi")


# @otzrouter.message(F.text == 'Lavozim takror')
# async def filter_byduplicates(message: Message):
#     res = await check_duplicates()
#     # ['code3', 'code3_name', 'branchName', 'depName', 'depCode', 'profName', 'profCode', 'rate_count', 'rate_count_bp', 'dublicate_count']
#     # cols = res.columns.tolist()
#     # group = res.groupby('branchName')['dublicate_count'].sum()

#     with pd.ExcelWriter("otz/duplicates.xlsx") as writer:
#         group.to_excel(writer, sheet_name="duplicate")
    
#     file_path = FSInputFile('otz/duplicates.xlsx')
#     await message.answer_document(file_path, caption="Ma'lumotlar duplicates.xlsx fayliga saqlandi")
#     # print(group)
#     # await message.answer("Biz lavozim duplicates ni ketshirmoqdamiz")
#     # await message.answer(f"Regionlar bo'yicha \n {group}")
















    