""" consumes and stores data """

import requests
import json
from datetime import datetime, timedelta
today = datetime.now()
last_month = today - timedelta(days=30)



base_url = "https://api.rawg.io/api/games/3498"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9"}

req = requests.get(base_url, params=api_key)
print(req.json())