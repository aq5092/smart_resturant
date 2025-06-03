
import requests
TOKEN = "4620|xDz0N9JvIiMBB7TQYQwSmqar7cbXKjTIDo9eU4ha"
    
async def GetHRP():
    url = f"https://b-hr.uzautomotors.com/api/position-description-detail"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
 # response = requests.get("https://b-hr.uzautomotors.com/api/test")
    response = requests.get(url, headers=headers)
    data = response.json()
    return data