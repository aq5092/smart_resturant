import requests

async def get_Data(url):
    response = requests.post("https://b-hr.uzautomotors.com/api/login", data={
        'name': "AQ5092",
        'password': 'Qwert789+654'
    })
    
    data = response.json()
    token = data['token']

    # token = "4718|k7wkvHDYlJCSalg2jS9wtH59YPU88kxLRM47aua1"
    
    
