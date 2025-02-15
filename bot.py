# -*- coding: utf-8 -*-

import requests
import time

ACCESS_TOKEN = "EAA4SghyFqQABO5jCEXEVwCvEVg88NaaTdkxZCRbHJu0XIJ4ct4IoN5jdiZALOuTS7F0lcdpZBQ0LPPNUPhErdyF9CCg3XtCfwY4YHbebbQ9YYO8wNYqT1dG8HYuETHEpVYZA2Y0ZBS3BwUe0YicOj6XzfVBgAtGqK0qZACEuzAqzO5yrxNmIyMOMY8Y3ZAkN17ZCGWUG4b8KEQwZBWnfAvcuY5y2B"
PAGE_ID = "763593701787944"

def post_to_facebook():
    url = "https://graph.facebook.com/{}/feed".format(330385883501389)
    params = {
        "message": " منشور تلقائي من البوت!",
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, params=params)
    print(response.json())

while True:
    post_to_facebook()
    time.sleep(3600)  
