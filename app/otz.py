import pandas as pd
import requests
TOKEN = "4637|qXz7unlwh8x1SjarXtsWWLR1Kw2QfP25Q9wgykXn"
    
async def check_lavozim():
    url = f"https://b-hr.uzautomotors.com/api/position-description-detail"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
 # response = requests.get("https://b-hr.uzautomotors.com/api/test")
    response = requests.get(url, headers=headers)
    data = response.json()
   
    if data:
        # print(data)
        df_yoqlar = pd.DataFrame(data['not_exist_position_description'])
        df_borlar = pd.DataFrame(data['exist_position_description'])
        # jami = len(df_borlar)+ len(df_yoqlar)
        # # Summarize the DataFrames to avoid long messages
        # borlar_count = len(df_borlar)
        # yoqlar_count = len(df_yoqlar)
        response = [df_borlar, df_yoqlar]
        return response
    else:
        print('Malumot yoq')
    