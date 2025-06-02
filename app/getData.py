import httpx
import pandas as pd

async def GetHRP(url_value):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://b-hr.uzautomotors.com/api" + url_value)
        return response.json()


