
#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_caching import Cache
from auth import User
from engine import FileStorage as fs
import api_requests


storage = fs()
storage.reload()

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cache = Cache(app)
next_page = ''


@app.route('/', strict_slashes=False)
# @cache.cached(timeout=50)
def index():
    """ homepage: just displays the games"""
    # testing
    data = api_requests.get_index()
    return render_template('index.html', data=data)


@app.route('/details/<int:id>')
def details(id):
    """ displayes information about a specific game """
    info = api_requests.get_index(id)
    screenshot = api_requests.screenshot(id)
    return render_template('details.html', info=info, screenshot=screenshot)

@app.route('/profile', strict_slashes=False)
def profile():
    """ displayes the user profile if user is logged in """
    return render_template('profile.html')



@app.route('/register',methods=['GET','POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        new_user = User(request.form['name'], request.form['email'], request.form['pass'])
        storage.new(new_user)
        storage.save()
        flash("you've resgister")
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)