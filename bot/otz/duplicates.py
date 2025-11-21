import requests
import pandas as pd
async def check_duplicates():
    response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
        'name': "AQ5092",
        'password': 'Qwert789+654'
    })
    
    data = response.json()
    token = data['token']
    url = f"https://b-hr.uzautomotors.com/api/position-description-dublicate-detail"
    headers = {
        "Authorization": f"Bearer {token}"
    }
 # response = requests.get("https://b-hr.uzautomotors.com/api/test")
    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        df = pd.DataFrame(data)
            # df_yoqlar = pd.DataFrame(data['not_exist_position_description'])
            # df_borlar = pd.DataFrame(data['exist_position_description'])
            # # jami = len(df_borlar)+ len(df_yoqlar)
            # # # Summarize the DataFrames to avoid long messages
            # # borlar_count = len(df_borlar)
            # # yoqlar_count = len(df_yoqlar)
            # response = [df_borlar, df_yoqlar]
            # return response
        return df
    else:
        print('Malumot yoq')