import requests
import json

CF_COOKIE_ON = False # if you want to turn on you need to setup https://github.com/zfcsoftware/cf-clearance-scraper

def get_cf_cookie():
    if CF_COOKIE_ON:
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