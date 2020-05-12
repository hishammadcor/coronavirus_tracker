from flask import Flask, render_template
import requests
import json


app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def data():

    url = "https://api.thevirustracker.com/free-api?countryTotals=ALL"
    response = requests.request("GET", url=url)
    df = json.loads(response.text)

    return render_template("base.html", data = df)

# @app.route('/country', methods = {'GET', 'POST'})
#
# def country_data():
#
#     url = "https://api.thevirustracker.com/free-api?countryTotal=US"
#     url= "https://api.thevirustracker.com/free-api?countryTimeline=US"
