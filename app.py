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

@app.route("/", methods=('GET', 'POST'))
def search():
	if request.method == 'POST':
		searchResults = request.form["whatToSearch"]
		subreddit = request.form["submitSearch"]
		
		if searchResults == "postsSelect":
			return redirect(url_for('.posts', id = subreddit))
		elif searchResults == "subredditSelect":
			return redirect(url_for('.subreddits', id = subreddit))
	return render_template("search.html")

@app.route('/posts/<id>')
def posts(id):
	subreddit = id
	result = bot.search_posts(subreddit)
	print("Got result back...")
	title = "Top Hottest Posts on {}".format(subreddit.capitalize())

	return render_template("index.html", Title=title, result=result)

@app.route('/subreddits/<id>')
def subreddits(id):
	subreddit = id
	result = bot.search_subs(subreddit)
	print("Got result back...")
	title = "Top Subreddits that match {}".format(subreddit.capitalize())

	return render_template("index.html", Title=title, result=result)