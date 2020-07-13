import requests
from requests_oauthlib import OAuth1
from .constants import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def send_tweet(tweet_text: str):
	url = f'https://api.twitter.com/1.1/statuses/update.json?status={tweet_text}'
	auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	response = requests.post(url, auth=auth)
