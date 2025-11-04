import pandas as pd
import requests

async def check_perevod():
    response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
        'name': "AQ5092",
        'password': 'Qwert789+654'
    })
    if response.status_code != 200:
        print('Login failed')
        return

    data = response.json()
    token = data.get('token')
    if not token:
        print('Token not found')
        return

    url = "https://b-hr.uzautomotors.com/api/rp-data-now"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('Failed to get online data')
        return
    online = pd.DataFrame(response.json())

    # If you want data for a different period, change the endpoint or add parameters here
    url2 = "https://b-hr.uzautomotors.com/api/rp-data-filter?year=2025&month=Iyul"
    headers2 = {"Authorization": f"Bearer {token}"}
    response2 = requests.get(url2, headers=headers2)
    if response2.status_code != 200:
        print('Failed to get last data')
        return
    last = pd.DataFrame(response2.json())

    if not online.empty and not last.empty:
        merged = online.merge(
            last,
            how='left',
            left_on=['tabel','department_code', 'lavozim_kodi'],
            right_on=['tabel','kod', 'lavozim_kodi'],
            indicator=True
        )
        mismatch = merged[merged['_merge'] == 'left_only']
        mismatch = mismatch[['tabel', 'boshqarma_nomi_x', 'bolimi_x', 'kod', 'lavozimi_x']]
        
        return mismatch
    else:
        print('Malumot yoq')
