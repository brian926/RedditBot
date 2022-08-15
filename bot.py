import praw
import yaml

def bot_login():
	config = yaml.safe_load(open("config.yml"))
	"""The login info for the bot which is stored in r."""
	r = praw.Reddit(username = config['username'],
		client_id = config['client_id'],
		client_secret = config['client_secret'],
		user_agent = "Comment responder")
	print("Logged in!")
	return r

def posts(subreddit):
	r = bot_login()
	print("Obtaining 25 comments...")
	
	subreddit = r.subreddit(subreddit)
	news_list = {}

	for submission in subreddit.hot(limit=25):
		news_list[submission.title] = "https://www.reddit.com" + submission.permalink
	return news_list

def subreddits(subreddit):
	r = bot_login()
	print("Obtaining subreddits like...")
	
	subs = r.subreddits.search_by_name(query=subreddit)
	sub_list = {}
	
	for submission in subs:
		sub_list[submission.display_name] = submission.public_description
	return sub_list

def top(subreddit, timeResult="all"):
	r = bot_login()
	print("Obtaining top posts...")

	posts = r.subreddit(subreddit).top(time_filter=timeResult)
	posts_list = {}

	for post in posts:
		posts_list[post.title] = "https://www.reddit.com" + post.permalink
	return posts_list