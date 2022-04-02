import os
import openai
import yaml

config = yaml.safe_load(open("config.yml"))
openai.api_key = config['openai_secret']

def index(news):
	response = openai.Completion.create(
		engine="text-curie-001",
		prompt=summarize(news),
		temperature=0.6,
		top_p=1,
		max_tokens=250,
		)
	return response.choices[0].text

def summarize(news):
	return """
	Summarize the following:
	{}
	""".format(news)
