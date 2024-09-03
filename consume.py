""" consumes and stores data """

import requests
import json
from datetime import datetime, timedelta
import os
today = datetime.now()
last_month = today - timedelta(days=30)


key = os.getenv("API_KEY")
base_url = "https://api.rawg.io/api/games/3498"
api_key = {"key": key}

req = requests.get(base_url, params=api_key)
print(req.json())