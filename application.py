from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField
from appconfig import AccountKey, DATA_URL, secretkey
import requests
import json
import datetime
from pytz import timezone

headers = {
	'accountkey': AccountKey
}

# instantiate app objects
application = Flask(__name__)
bootstrap = Bootstrap(application)

# class submit form button
class SubmitForm(FlaskForm):
	submit = SubmitField("Submit")

#secretkey
application.config['SECRET_KEY'] = secretkey

# set timezone
timezone = timezone("Asia/Singapore")

# routes
@application.route('/', methods=['GET','POST'])
def index():
	form = SubmitForm()
	# this runs only if form is submitted
	if form.validate_on_submit():
		# gets UTC time then converts to local time (+8)
		time = " ".join([datetime.datetime.now().astimezone(timezone).strftime("%A %d-%m-%Y %H:%M:%S"), 
			"(SGT)"])
		# converts to json objects using the HTTP request from DataMall
		incidents = json.loads(requests.request("GET", DATA_URL, headers=headers).text)
		# each value is an incident, 
		# we pass this as a dictionary to be iterated with the template
		try:
			values = incidents["value"]
		except KeyError:
			return render_template("404.html"), 404
		return render_template("index.html", values=values, time=time, form=form)
	else:
		return render_template("index.html", form=form)

@application.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# run app
if __name__ == "__main__":
	application.run()