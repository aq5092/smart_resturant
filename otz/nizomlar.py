from app.get_data import get_Data
import pandas as pd
async def check_nizomlar():
    data = await get_Data("department-regulation-detail")
    if data:
        # print(data)
        df_yoqlar = pd.DataFrame(data['not_exist_department_regulations'])
        df_borlar = pd.DataFrame(data['exist_department_regulations'])
        # jami = len(df_borlar)+ len(df_yoqlar)
        # # Summarize the DataFrames to avoid long messages
        # borlar_count = len(df_borlar)
        # yoqlar_count = len(df_yoqlar)
        response = [df_borlar, df_yoqlar]
        return response
    else:
        print('Malumot yoq')
    
