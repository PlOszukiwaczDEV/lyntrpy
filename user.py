import requests
import os
import utils.headers
import json
import utils

def edit_profile(username : str = None, bio : str = "Nothing here yet..."):
    data = {
        'bio': bio,
        'username': username
    }

    r = requests.patch('https://lyntr.com/api/profile', cookies=cookies, headers=utils.headers.profile_headers, data=data)
    return r
def get_user_profile(profileHandle):
    """
    Get a profile via thier handle
    """

    params = {
        'handle': profileHandle
    }

    r = requests.get('https://lyntr.com/api/profile', params=params, cookies=cookies, headers=utils.headers.profile_headers)
    return r
def delete_user():
    pass