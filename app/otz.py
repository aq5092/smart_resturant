from app.getData import GetHRP
import pandas as pd

class CheckLavozim:
    # url = '/position-description-detail'
    

    @staticmethod
    async def get_data():
        url = '/test'
        data = await GetHRP(url)
        print(data)
        if not data:
            return None
        # lv_yoq = data[0]
        # lv_bor = data[1]
        return data
    