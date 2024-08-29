import requests

base_url = "https://api.rawg.io/api/games"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9"}

data = {}

req = requests.get(base_url, api_key)
def get_index(next=None):
    if next:
        req = requests.get(next)
        data['results'] = data['results'] + req.json()['results']
    else:
        req = requests.get(base_url, api_key)
        data['results'] = req.json()['results']
        data['next']=req.json()['next']
    return data





