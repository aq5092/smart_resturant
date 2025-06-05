import requests

async def get_Data(url):
    response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
        'name': "AQ5092",
        'password': 'Qwert789+654'
    })
    
    data = response.json()
    token = data['token']

    # token = "4718|k7wkvHDYlJCSalg2jS9wtH59YPU88kxLRM47aua1"
    urls = f"https://b-hr.uzautomotors.com/api/{url}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(urls, headers=headers)
    data = response.json()
    if data:
    
        return data
    else:
        print('Malumot yoq')
        return None
    
