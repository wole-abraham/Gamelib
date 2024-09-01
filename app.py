
#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, request
from flask_caching import Cache
import api_requests

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
next_page = ''


@app.route('/', strict_slashes=False)
@cache.cached(timeout=50)
def index():
    """ homepage: just displays the games"""
    # testing
    data = api_requests.get_index()
    return render_template('index.html', data=data)

def details(game_id):
    """ displayes information about a specific game """
    info = api_requests.get_index(game_id)
    return render_template('details.html', info=info)

@app.route('/profile', strict_slashes=False)
def profile():
    """ displayes the user profile if user is logged in """
    return render_template('profile.html')

@app.route('/logi`n', strict_slashes=False)
def login():
    """ authenication:
        basic auth 
    
        """
    return render_template('logout.html')

@app.route('/register', strict_slashes=False)
def register():
    """ create a new user """
    return render_template('register.html')

@app.route('/browse', strict_slashes=False)
def browse():
    return render_template('browse.html')

@app.route('/streams')
def streams():
    return 'streams'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)