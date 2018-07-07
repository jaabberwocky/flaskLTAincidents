from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import SubmitField
from appconfig import AccountKey, DATA_URL
import requests
import json
import datetime

headers = {
	'accountkey': AccountKey
}

# class submit form button
class SubmitForm(Form):
	submit = SubmitField("Submit")

app = Flask(__name__)
bootstrap = Bootstrap(app)
#secretkey
app.config['SECRET_KEY'] = "hellowtfwtfwtf1234"

# routes
@app.route('/', methods=['GET','POST'])
def index():
	form = SubmitForm()
	if form.validate_on_submit():
		time = str(datetime.datetime.now())
		incidents = json.loads(requests.request("GET", DATA_URL, headers=headers).text)
		values = incidents["value"]
		return render_template("index.html", values=values, time=time, form=form)
	else:
		return render_template("index.html", form=form)



# run app
if __name__ == "__main__":
	app.run(debug=True)