from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SubmitField
from appconfig import AccountKey, DATA_URL
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
class SubmitForm(Form):
	submit = SubmitField("Submit")

#secretkey
application.config['SECRET_KEY'] = "hellowtfwtfwtf1234"

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
		# each value is an incident
		values = incidents["value"]
		return render_template("index.html", values=values, time=time, form=form)
	else:
		return render_template("index.html", form=form)

# run app
if __name__ == "__main__":
	application.run()