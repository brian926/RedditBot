import praw
import time
import os
import requests
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

def run_bot(r, comments_replied_to):
	"""The bot searches thru 25 comments and if matched, replies."""
	print("Obtaining 25 comments...")

	for comment in r.subreddit('test').comments(limit=25):
		print(comment.body)
		#if "Chuck Norris" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
		#	print("Chuck Norris found!")
		#
		#	comment_reply = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
		#	comment.reply(comment_reply)
		#	print("Replied to comment " + comment.id)

		#	comments_replied_to.append(comment.id)
		

		with open("comments_replied_to.txt", "a") as f:
			f.write(comment.id + "\n")

	print("Sleeping for 10 seconds...")
	time.sleep(10)
	global run_time 
	run_time += 1

def get_saved_comments():
	"""Creates a file with comments id replied to inside"""
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to

comments_replied_to = get_saved_comments()
print(comments_replied_to)
r = bot_login()
run = True
run_time = 0

while run:
	run_bot(r, comments_replied_to)
	if run_time > 5:
		print("That enough Reddit for one day.\nNow shutting off...")
		run = False