import requests
from urllib.parse import urlencode, quote_plus
from requests_oauthlib import OAuth1
from .constants import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def send_tweet(tweet_text: str):
	url = f'https://api.twitter.com/1.1/statuses/update.json'
	params = {'status': f'{tweet_text} #Reminders'}
	auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	requests.post(url, params=params, auth=auth)
