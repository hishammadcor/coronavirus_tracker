from flask import Flask, render_template
import requests
import json


app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def data():

    url = "https://api.thevirustracker.com/free-api?countryTotals=ALL"
    url2 = "https://api.thevirustracker.com/free-api?global=stats"
    response_ALL = requests.request("GET", url=url)
    response_Global= requests.request("GET", url=url2)

    df = json.loads(response_ALL.text)
    df2 = json.loads(response_Global.text)

    return render_template("base.html", data1= df, data = df2 )

# @app.route('/country', methods = {'GET', 'POST'})
#
# def country_data():
#
#     url = "https://api.thevirustracker.com/free-api?countryTotal=US"
#     url= "https://api.thevirustracker.com/free-api?countryTimeline=US"
