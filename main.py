import flask
from flask import request
import os
import logging
from twilio.rest import Client

account_sid = "AC287c16e55134eae71daa6b288e6dde51"
auth_token = "f969a927d0a6704444a4a46979b66e04"

client = Client(account_sid, auth_token)

app = flask.Flask(__name__)

@app.route('/')
def root():
	lat = request.args['lat']

	message = client.messages.create(
	to="whatsapp:+917760329001",
	from_="whatsapp:+14155238886",
	body=lat
	)
	return ""



@app.errorhandler(500)
def server_error(e):
	logging.exception('An error occurred during a request.')
	return """
	An internal error I have no idea too bad too sad!!!!
	""".format(e), 500

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port=8080, debug=True)
