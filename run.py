from twitter_api import send_tweet
import csv

def get_tweet_text() -> str:
	tweet_file = open('./tweets.csv', 'r')
	reader = csv.reader(tweet_file)
	for entry in reader:
		print(entry)
	# Pull in text file
	# Randomly pick one
	# If it hasn't been one of the last 5 tweets
	# Tweet it
	# else grab a different tweet
	# Save index of that tweet



if __name__ == '__main__':
	send_tweet(get_tweet_text())


