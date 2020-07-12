import random


def get_tweet_text() -> str:
	# Parse available tweets
	tweet_file = open('./data/tweets.txt', 'r')
	content = tweet_file.readlines()
	content = [x.strip() for x in content]

	# Parse recent tweets
	recent_tweet_file_reader = open('./data/recent_tweets.txt', 'r')
	recent_tweet_content = recent_tweet_file_reader.readlines()
	recent_tweet_content = [x.strip() for x in recent_tweet_content]

	# Loop until we choose a tweet we haven't tweeted recently
	while True:
		choice = random.choice(content)
		if choice not in recent_tweet_content:
			break

	# Write current tweet to recent file
	recent_tweet_file_writer = open('./data/recent_tweets.txt', 'a')
	recent_tweet_file_writer.write(choice+'\n')

	# Close file readers
	recent_tweet_file_writer.close()
	recent_tweet_file_reader.close()

	remove_oldest_recent_tweet()

	return choice


def remove_oldest_recent_tweet():
	recent_tweet_file_reader = open('./data/recent_tweets.txt', 'r')
	recent_tweet_content = recent_tweet_file_reader.readlines()
	recent_tweet_content = [x.strip() for x in recent_tweet_content]

	# Clear out recents after 5 tweets
	if len(recent_tweet_content) > 5:
		recent_tweet_file_writer = open('./data/recent_tweets.txt', 'w')
		for index, line in enumerate(recent_tweet_content):
			# Don't write (delete) the first line since it's the oldest recent tweet
			if index != 0:
				recent_tweet_file_writer.write(line+'\n')
		recent_tweet_file_writer.close()

	recent_tweet_file_reader.close()
