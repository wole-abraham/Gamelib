#!/usr/bin/python3

import requests

base_url = "https://api.rawg.io/api/games/"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9", 'page_size': 2}

req = requests.get(base_url, params=api_key)
