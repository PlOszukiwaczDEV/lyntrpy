import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_cf_cookie():
    if os.getenv("CF_COOKIE_ENABLED") == "True":
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            "url": "https://lyntr.com",
            "mode": 'waf'
        }

        r = requests.post("http://localhost:3000/cf-clearance-scraper", headers=headers, data=json.dumps(data))
        return r
    else:
        return "Disabled"