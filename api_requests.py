""" consumes and stores data """

import requests
import os
import json
from app import db
from models import Game
from datetime import datetime, timedelta
today = datetime.now()
last_month = today - timedelta(days=30)

date_range = f"{last_month.strftime('%Y-%m-%d')},{today.strftime('%Y-%m-%d')}"
key = os.getenv('API_KEY')
base_url = "https://api.rawg.io/api/games"
api_key = {"key": key, 
        #    'dates': date_range,
           'ordering': '-added',  # Order by popularity (most added)
           
           'page_size': 40

}




def get_index(id=None, next=None):

    if id is None and next is None:
        req = requests.get(base_url, params=api_key)
        return req.json()

    if next:
        req = requests.get(next)
        return req.json()

    if id:
        game = Game.query.filter_by(id=id).first()

        if game is None:
            req = requests.get(base_url + f'/{id}', params=api_key).json()
            screenshot = requests.get(base_url + f'/{id}' + '/screenshots', params=api_key).json()['results']


            game = Game(id=req['id'], title=req['name'],
                        description=req['description'],
                        background_image=req['background_image'],
                        rating=req['rating'], website=req['website'],
                        screenshots =  [ x['image'] for x in screenshot]             
                        )
            db.session.add(game)
            db.session.commit()
            return game
        return game