#!/usr/bin/python3
from flask import render_template, url_for, redirect, request, flash, session
from flask_caching import Cache
from engine import User, Game
from api_requests import get_index, screenshot as sc
from app import app
from app import db


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cache = Cache(app)
next_page = ''


@app.route('/', strict_slashes=False)
# @cache.cached(timeout=50)
def index():
    """ homepage: just displays the games"""
    # testing
    global next_page
    data = get_index()
    next_page = data['next']
    if session.get('id'):
        user = User.query.filter_by(id=session['id']).first()
        return render_template('index.html', data=data, user=user)

    return render_template('index.html', data=data)

@app.route('/loadmore')
def load_more():
    global next_page
    print(next_page)
    page = get_index(next=next_page)
    next_page = page['next']
    print(next_page)
    return render_template('more_games.html', games=page)


@app.route('/details/<int:id>')
def details(id):
    """ displayes information about a specific game """
    info = get_index(id)
    screenshot = sc(id)
    return render_template('details.html', info=info, screenshot=screenshot)

@app.route('/profile', strict_slashes=False)
def profile():
    """ displayes the user profile if user is logged in """
    if session.get('id'):
        user = User.query.filter_by(id=session['id']).first()
        return render_template('profile.html', user=user)

    return render_template('profile.html')



@app.route('/register',methods=['GET','POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            return render_template('register.html', error='Username already exists')

        if User.query.filter_by(email=request.form['email']).first():
            return render_template('register.html', error="Email has already been used")

        new_user = User(username=request.form['username'],
                        email=request.form['email'],
                        password=request.form['password']
                        )
        db.session.add(new_user)
        db.session.commit()
        flash("you've resgister")
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        print(user.username)
        if user:
            if user.password == request.form['pass']:
                session['id'] = user.id
                return redirect(url_for('index'))

        else:
            return render_template('login.html', error='Username or Password is incorrect')
            
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
