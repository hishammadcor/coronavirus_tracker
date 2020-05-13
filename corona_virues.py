from flask import Flask,jsonify,render_template, request, redirect
import requests
import json
import numpy
import math
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def data():

    url = "https://api.thevirustracker.com/free-api?countryTotals=ALL"
    url2 = "https://api.thevirustracker.com/free-api?global=stats"
    response_ALL = requests.request("GET", url=url)
    response_Global= requests.request("GET", url=url2)

    df2 = json.loads(response_Global.text)
    df = json.loads(response_ALL.text)

    return render_template("base.html", data1= df, data2 = df2 )

@app.route('/country',methods = ["GET" , "POST"])
def plot():

    country = request.form["country"]
    url = "https://api.thevirustracker.com/free-api?countryTotal=" + country
    url2 = "https://api.thevirustracker.com/free-api?countryTimeline="+ country
    response_Total = requests.get(url)
    response_Timeline= requests.request("GET", url=url2)

    dg =  json.loads(response_Timeline.text)
    data3= json.loads(response_Total.text)

    D,f = next(iter(dg["timelineitems"][0].items()))

    daily_cases= list()
    for days in dg["timelineitems"]:
        for day in days:
            if day == 'stat':
                break
            else:
                y = days[day]["new_daily_cases"]
                daily_cases.append(y)

    fig = plt.figure(figsize=(8, 6))
    plt.plot(daily_cases,'b.', label= 'Daily cases')
    plt.xlabel("Number of days since "+ D)
    plt.ylabel("Number of cases")
    img = plt.savefig('/home/hisham/Documents/coronavirus/static/imgs/' + country)

    return render_template("Country.html", data3=data3, country= country, url = '/home/hisham/Documents/coronavirus/static/imgs/' + country)


# # plt.plot(Daily_cases(),'b.', label= 'Dailycases')
# # plt.xlabel("Number of days since "+ D)
# # plt.ylabel("Number of cases")
# # plt.show()
