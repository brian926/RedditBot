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
		subreddit = request.form['subreddit']
		print(subreddit)
		if not subreddit:
			flash('Enter a subreddit')
		else:
			return redirect(url_for('.test', id = subreddit))
	return render_template("search.html")

@app.route('/results/<id>')
def test(id):
	subreddit = id
	result = bot.awaken_bot(subreddit)
	print("Got result back...")

	return render_template("index.html", Title=subreddit.capitalize(), result=result)