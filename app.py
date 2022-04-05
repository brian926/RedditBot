import bot
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
	result = bot.awaken_bot()
	print("Got result back...")
	print(result)
	return render_template("index.html", result=result)