import flask
from flask import request
import os
import logging
from twilio.rest import Client

account_sid = "XXXXXX"
auth_token = "XXxXXX"

client = Client(account_sid, auth_token)

app = flask.Flask(__name__)

@app.route('/')
def root():
	lat = request.args['lat']
	lon = request.args['longi']
	message = client.messages.create(
	to="whatsapp:+917760329001",
	from_="whatsapp:+14155238886",
	body="Cyclist has fallen. Location is " + lat + ", " + lon + ". Link to location: http://google.com/maps/place/12%C2%B053'16.3%22N+77%C2%B045'06.6%22E/@12.8878072,77.7515759,18.49z/data=!4m5!3m4!1s0x0:0x0!8m2!3d12.887848!4d77.751824"
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
