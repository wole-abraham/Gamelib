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
key = os.getenv('API_KEY') # gets the api key stored in my environment varible
base_url = "https://api.rawg.io/api/games"     # base endpoint from the api
api_key = {"key": key, 
           'ordering': '-added',  # Order by popularity (most added)
           'page_size': 40
           }


def get_index(id=None, next=None):
    """ 
        queries the api:
        returns all games by default
        id: returns info for specific game
        next: 'next' is a link to another set of game, passing this returns those games
    """

    if id is None and next is None:
        req = requests.get(base_url, params=api_key)
        return req.json()

    if next:
        req = requests.get(next)
        return req.json()

    if id:
        game = Game.query.filter_by(id=id).first() # checks the database if the game already exists through the id
        if game is None:  # if the game doesnt exist in the database
            req = requests.get(base_url + f'/{id}', params=api_key).json() # this gets the specific game through the api
            screenshot = requests.get(base_url + f'/{id}' + '/screenshots', params=api_key).json()['results'] # these are screenshots for the game 
                                                                                                              # the endpoint for the games/details only one image 
                                                                                                              # so we have to grap more image links through this endpoint


            game = Game(id=req['id'], title=req['name'],            # stores the data from the api into the Game object
                        description=req['description'],             # so next time we query for this specific game it won't need to query the api
                        background_image=req['background_image'],
                        rating=req['rating'], website=req['website'],
                        screenshots =  [ x['image'] for x in screenshot]             
                        )
            db.session.add(game) # loads the game object attr into a session for the db
            db.session.commit() # saves the game
            return game
        return game