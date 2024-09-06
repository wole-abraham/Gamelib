from uuid import uuid4
from datetime import datetime

class User():

    """ Basic User data """
    def __init__(self, username, email, password, games=None, created_at=None, **kwargs):
        self.id = uuid4()
        self.username = username
        self.email = email
        self.password = password
        self.games = []
        self.created_at = datetime.now()

    def add_game(self, id):
        self.games.append(id)
        
    def to_dict(self):

        return {'username': self.username,
                'email': self.email,
                'password': self.password,
                'games': self.games,
                'self.created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")}
    
    @classmethod
    def to_obj(cls, dict_data):
        return cls(dict_data['username'], dict_data['email'], dict_data['password'], dict_data['games'], dict_data['self.created_at'])


