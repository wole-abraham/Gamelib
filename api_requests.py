""" consumes and stores data """

import requests
import json
from datetime import datetime, timedelta
today = datetime.now()
last_month = today - timedelta(days=30)

date_range = f"{last_month.strftime('%Y-%m-%d')},{today.strftime('%Y-%m-%d')}"

base_url = "https://api.rawg.io/api/games"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9", 
           'dates': date_range,
           'ordering': '-added',  # Order by popularity (most added)
           
           'page_size': 30

}

def get_index(data=None):
    if data:
        req = requests.get(base_url + f'/{data}', params=api_key)
        return req.json()

    req = requests.get(base_url, params=api_key)
    return req.json()['results']

def screenshot(data=None):
    if data:
        req = requests.get(base_url + f'/{data}/screenshots', params=api_key)
        print(req.json())
        return req.json()['results']




