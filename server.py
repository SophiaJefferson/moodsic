import sys
from flask import Flask, render_template, request, redirect, Response, send_from_directory
import random, json

app = Flask(__name__)

@app.route('/')
def index():
	# serve index template
	return render_template('index.html', name='Joe')

@app.route('/receiver', methods = ['POST'])
def receiver():
	# read json + reply
	# data = request.get_json()
	# app.logger.debug('A value for debugging')

	return render_template('index.html', name='Joe')

# @app.route('/<appName>')
# def name(appName=None):
	# read json + reply
	# data = request.get_json()
	# app.logger.debug('A value for debugging')

	# return render_template('index.html', appName=appName)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
    # return render_template('index.html', appName=name)

if __name__ == '__main__':
	app.run()