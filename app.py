import bot
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/all")
def all():
	subreddit = 'all'
	result = bot.posts(subreddit)
	print("Got result back...")
	title = "Top Hottest Posts on {}".format(subreddit.capitalize())
	return render_template("posts.html", Title=title, result=result, subreddit=subreddit)

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
	result = bot.posts(subreddit)
	print("Got result back...")
	title = "Top Hottest Posts on {}".format(subreddit.capitalize())
	return render_template("posts.html", Title=title, result=result, subreddit=subreddit)

@app.route('/subreddits/<string:id>')
def subreddits(id):
	subreddit = id
	result = bot.subreddits(subreddit)
	print("Got result back...")
	title = "Top Subreddits that match {}".format(subreddit.capitalize())
	return render_template("subreddits.html", Title=title, result=result)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 404