import requests

base_url = "https://api.rawg.io/api/games"
api_key = {"key": "4f87adae5f3c405fbd2e86a44af08ec9"}
image = []
def get_index():
    req = requests.get(base_url, api_key)
    res = req.json().get('results')
    for shots in res:
        images = shots['short_screenshots'][0]['image']
        image.append(images)
    
    return image



