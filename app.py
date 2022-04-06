import bot
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/news")
def news():
	subreddit = 'news'
	result = bot.awaken_bot(subreddit)
	print("Got result back...")

	return render_template("index.html", Title=subreddit.capitalize(), result=result)

@app.route("/all")
def all():
	subreddit = 'all'
	result = bot.awaken_bot(subreddit)
	print("Got result back...")

	return render_template("index.html", Title=subreddit.capitalize(), result=result)