from twitter_api import send_tweet
import random

def get_tweet_text() -> str:
	tweet_file = open('./data/tweets.txt', 'r')
	content = tweet_file.readlines()
	content = [x.strip() for x in content]
	print(random.choice(content))

	# recent_tweet_file = open('.')

	# Pull in text file
	# Randomly pick one
	# If it hasn't been one of the last 5 tweets
	# Tweet it
	# else grab a different tweet
	# Save index of that tweet



if __name__ == '__main__':
	send_tweet(get_tweet_text())


