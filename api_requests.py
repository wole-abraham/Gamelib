""" consumes and stores data """

import requests
import os
import json
from app import db
from engine import Game
from datetime import datetime, timedelta
today = datetime.now()
last_month = today - timedelta(days=30)

date_range = f"{last_month.strftime('%Y-%m-%d')},{today.strftime('%Y-%m-%d')}"
key = os.getenv('API_KEY')
base_url = "https://api.rawg.io/api/games"
api_key = {"key": key, 
           'dates': date_range,
           'ordering': '-added',  # Order by popularity (most added)
           
           'page_size': 30

}

def get_index(data=None, next=None):
    if data:
        req = requests.get(base_url + f'/{data}', params=api_key)
        data = req.json()
        game = Game(id=data['id'], title=data['name'],
                    description=data['description'], background_image=data['background_image'],
                    rating=data['rating'], website=data['website']
                    )
        return req.json()
    
    if next:
        req = requests.get(next)
        data = req.json()
        return data

    req = requests.get(base_url, params=api_key)
    return req.json()

def screenshot(data=None):
    if data:
        req = requests.get(base_url + f'/{data}/screenshots', params=api_key)
        print(req.json())
        return req.json()['results']
