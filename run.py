from logic.twitter_api import send_tweet
from logic.tweet_prep import get_tweet_text


if __name__ == '__main__':
	send_tweet(get_tweet_text())
