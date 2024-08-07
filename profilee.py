import requests
import os
import utils.headers
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Load cookies from environment variables
cookies = {
    '_TOKEN__DO_NOT_SHARE': os.getenv('TOKEN'),
    'temp-discord-token': os.getenv('temp-discord_token'),
    'cf_clearance': os.getenv('cf_clearance'),
}

def get_profile(profileHandle):
    """
    Get a profile via thier handle
    """

    params = {
        'handle': profileHandle
    }

    r = requests.get('https://lyntr.com/api/profile', params=params, cookies=cookies, headers=utils.headers.profile_headers)
    return r
def edit_profile(username : str = None, bio : str = "Nothing here yet..."):
    data = {
        'bio': bio,
        'username': username
    }

    r = requests.patch('https://lyntr.com/api/profile', cookies=cookies, headers=utils.headers.profile_headers, data=data)
    return r
