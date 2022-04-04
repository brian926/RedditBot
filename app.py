import praw
import time
import os
import requests
import yaml
import openSummary
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

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
	print("Obtaining 25 comments...")
	
	subreddit = r.subreddit('news')
	news_list = []

	for submission in subreddit.hot(limit=25):
		if submission.id not in comments_replied_to:
			#print(submission.title)
			#news_ai = openSummary.index(submission.title)
			#print(news_ai)
			#print(submission.url)
			#print('\n')

			news_list.append(submission.title)
			comments_replied_to.append(submission.id)
		

		with open("comments_replied_to.txt", "a") as f:
			f.write(submission.id + "\n")

	print("Sleeping for 10 seconds...")

	return news_list

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to

def awaken_bot():
	comments_replied_to = get_saved_comments()
	print(comments_replied_to)
	r = bot_login()

	results = run_bot(r, comments_replied_to)
	return results


@app.route("/")
def index():
	result = awaken_bot()
	print("Got result back...")
	print(result)
	return render_template("index.html", result=result)