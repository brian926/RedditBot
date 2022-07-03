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

def run_bot(r, subreddit):
	print("Obtaining 25 comments...")
	
	subreddit = r.subreddit(subreddit)
	news_list = []
	
	for submission in subreddit.hot(limit=25):
		news_list.append(submission.title)

	return news_list

def search(r, subreddit):
	print("Obtaining 25 comments...")
	
	subs = r.subreddits.search_by_name(query=subreddit)
	sub_list = []
	
	for submission in subs:
		sub_list.append(submission.display_name)

	return sub_list

def search_posts(subreddit):
	
	r = bot_login()
	
	results = run_bot(r, subreddit)
	
	return results

def search_subs(subreddit):
	r = bot_login()
	results = search(r, subreddit)

	return results