import bot
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/all")
def all():
	subreddit = 'all'
	result = bot.search_posts(subreddit)
	print("Got result back...")

	return render_template("posts.html", Title=subreddit.capitalize(), result=result)

@app.route("/", methods=('GET', 'POST'))
def search():
	if request.method == 'POST':
		searchResults = request.form["whatToSearch"]
		subreddit = request.form["submitSearch"]
		
		if searchResults == "postsSelect":
			return redirect(url_for('.posts', id = subreddit))
		elif searchResults == "subredditSelect":
			return redirect(url_for('.subreddits', id = subreddit))
	return render_template("index.html")

@app.route('/posts/<string:id>')
def posts(id):
	subreddit = id
	result = bot.search_posts(subreddit)
	print("Got result back...")
	title = "Top Hottest Posts on {}".format(subreddit.capitalize())

	return render_template("posts.html", Title=title, result=result)

@app.route('/subreddits/<string:id>')
def subreddits(id):
	subreddit = id
	result = bot.search_subs(subreddit)
	print("Got result back...")
	title = "Top Subreddits that match {}".format(subreddit.capitalize())

	return render_template("subreddits.html", Title=title, result=result)