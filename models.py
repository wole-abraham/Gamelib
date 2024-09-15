from app import db
from sqlalchemy import JSON

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    games = db.relationship('UserGame', back_populates='user')

    def __repr__(self):

        return f'<User {self.username}>'

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable = True)
    background_image = db.Column(db.Text, nullable=True)
    screenshots = db.Column(JSON, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    website = db.Column(db.Text, nullable=True)

    users = db.relationship('UserGame', back_populates='game')

class UserGame(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    user = db.relationship('User', back_populates='games')

    game = db.relationship('Game',  back_populates='users')



