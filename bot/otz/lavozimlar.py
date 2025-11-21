import pandas as pd
import requests
 
async def check_lavozim():
    response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
        'name': "AQ5092",
        'password': 'Qwert789+654'
    })
    
    data = response.json()
    token = data['token']
    # print(token)
    
    url = f"https://b-hr.uzautomotors.com/api/position-description-detail"
    headers = {
        "Authorization": f"Bearer {token}"
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


# async def get_token():
#     response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
#         'name': "AQ5092",
#         'password': 'Qwert789+654'
#     })
#     data = response.json()
#     token = data['token']
#     return token


# TOKEN = "4677|8rycRElMCA7zdpJ86bWNtarCdfGyq0oiDXgBMdnj"