from app.get_data import get_Data
import pandas as pd 
import aiohttp

async def get_hreport():
    data = await get_Data("rp-data-api")
    
    if data:
        df = pd.DataFrame(data)
        return df
    else:
        print('Malumot yoq')
        return None
    
# async def check_rp():
#     online = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQKqyUbbN5yOb5-YoI0KJ7R7NF1h6sSZ5VZgKhQFjYiqZgGVJVRhU8XJTZugo7vzNhABu6KpvTkhABV/export?format=csv")
#     if online:
#         return online
#     else:
#         print("Ma'lumot yoq")
#         return None


        

    
# response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
    #     'name': "AQ5092",
    #     'password': 'Qwert789+654'
    # })
    
    # data = response.json()
    # token = data['token']

    # # token = "4718|k7wkvHDYlJCSalg2jS9wtH59YPU88kxLRM47aua1"
    # url = f"https://b-hr.uzautomotors.com/api/rp-data-api"
    # headers = {
    #     "Authorization": f"Bearer {token}"
    # }
    # response = requests.get(url, headers=headers)
    # data = response.json()