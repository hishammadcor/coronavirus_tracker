from flask import Flask,jsonify,render_template, request, redirect, url_for, Blueprint
import requests
import json
import numpy
import math
import matplotlib.pyplot as plt
from scipy import stats


bp = Blueprint('corona_virues', __name__)

@bp.route('/', methods = ['GET', 'POST'])
def data():

    url = "https://api.thevirustracker.com/free-api?countryTotals=ALL"
    url2 = "https://api.thevirustracker.com/free-api?global=stats"
    response_ALL = requests.request("GET", url=url)
    response_Global= requests.request("GET", url=url2)

    df2 = json.loads(response_Global.text)
    df = json.loads(response_ALL.text)

    return render_template("base.html", data1= df, data2 = df2 )

@bp.route('/country',methods = ["GET" , "POST"])
def plot():

    country = request.form["country"]
    url = "https://api.thevirustracker.com/free-api?countryTotal=" + country
    url2 = "https://api.thevirustracker.com/free-api?countryTimeline="+ country
    response_Total = requests.get(url)
    response_Timeline= requests.request("GET", url=url2)

    dg =  json.loads(response_Timeline.text)
    data3= json.loads(response_Total.text)

    D,f = next(iter(dg["timelineitems"][0].items()))

    first_day = f["new_daily_cases"]
    log_first_day = math.log(first_day)

    daily_cases= list()
    daily_deaths= list()
    for days in dg["timelineitems"]:
        for day in days:
            if day == 'stat':
                break
            else:
                cases= days[day]["new_daily_cases"]
                deaths= days[day]["new_daily_deaths"]
                daily_cases.append(cases)
                daily_deaths.append(deaths)

    plt.figure()
    plt.plot(daily_cases,'b.', label= "Daily cases")
    plt.xlabel("Number of days since "+ D)
    plt.ylabel("Number of cases")
    plt.title("Daily cases in " + country)
    plt.grid(True)
    img = plt.savefig('/home/hisham/Documents/coronavirus/corona/static/imgs/' + country+'_cases')

    plt.figure()
    plt.plot(daily_deaths,'r.', label= "Daily Deaths")
    plt.xlabel("Number of days since "+ D)
    plt.ylabel("Number of deaths")
    plt.title("Daily Deaths in " + country)
    plt.grid(True)
    img = plt.savefig('/home/hisham/Documents/coronavirus/corona/static/imgs/' + country+'_deaths')

    def log_cases():
        log_daily_cases= list()
        for days in dg["timelineitems"]:
            for day in days:
                if day == 'stat':
                    break
                else:
                    y = days[day]["new_daily_cases"]
                    if  y == 0:
                        log_daily_cases.append(y)
                    else:
                        i = math.log10(y)
                        log_daily_cases.append(i)
        return log_daily_cases

    def days():
        days = list()
        for i in range(len(log_cases())):
            days.append(i)
        return days

    slope, intercept, r_value, p_value, std_err = stats.linregress(days(), log_cases())
    R = 10 ** (slope *6)

    def daily_R():
        R = list()
        for i,j in zip(log_cases(), days()):
            if j != 0:
                R_0= 10 ** ((6*(i-log_first_day))/j)
                R.append(R_0)
        return R

    plt.figure()
    plt.plot(daily_R(),'g.', label= "Daily R_0")
    plt.xlabel("Number of days since "+ D)
    plt.ylabel("Reproductive Number")
    plt.title("Daily Reproductive Number in " + country)
    plt.grid(True)
    img = plt.savefig('/home/hisham/Documents/coronavirus/corona/static/imgs/' + country+'_R')



    return render_template("Country.html", data3=data3, country= country, cases = url_for('static', filename = '/imgs/'+country+'_cases.png')
                                            , deaths = url_for('static', filename = '/imgs/'+country+'_deaths.png'), Reproductive=R
                                            , DailyR = url_for('static', filename = '/imgs/'+country+'_R.png'))
