
#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, request
import api_requests
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ homepage: just displays the games"""
    # testing 
    next = request.args.get('next')
    data  = api_requests.get_index(next)
    return render_template('index.html', data=data)

@app.route('/more')
def more():
    next = request.args.get('next')
    return redirect(url_for('index', next=next))

@app.route('/details', strict_slashes=False)
def details():
    """ displayes information about a specific game """
    return render_template('details.html')

@app.route('/profile', strict_slashes=False)
def profile():
    """ displayes the user profile if user is logged in """
    return render_template('profile.html')

@app.route('/login', strict_slashes=False)
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