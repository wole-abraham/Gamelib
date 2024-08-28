#!/usr/bin/python3

from flask import Flask, render_template
import requests


app = Flask(__name__)

base_url = "https://api.rawg.io/api/games/3498/"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9"}


@app.route('/', strict_slashes=False)
def index():
    req = requests.get(base_url, params=api_key)

    return render_template('index.html', game=req.json().get('name'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
