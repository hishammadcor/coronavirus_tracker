from flask import Flask,jsonify,render_template
import pandas as pd
import requests
import simplejson
import json

app = Flask(__name__)
@app.route("/")
def home():
    url = "https://api.thevirustracker.com/free-api?global=stats"
    try:
        r = requests.get(url)
    except requests.ConnectionError:
       return "Connection Error"

    response = r.text
    data = json.loads(response)
    total_cases=data["results"][0]["total_cases"]
    total_recovered= data["results"][0]["total_recovered"]
    total_deaths= data["results"][0]["total_deaths"]
    total_new_cases_today = data["results"][0]["total_new_cases_today"]
    total_new_deaths_today = data["results"][0]["total_new_deaths_today"]
    total_affected_countries= data["results"][0]["total_affected_countries"]

    return render_template("base 1.html" ,total_cases=total_cases,total_recovered=total_recovered,total_deaths=total_deaths,total_new_cases_today=total_new_cases_today,total_new_deaths_today=total_new_deaths_today,total_affected_countries=total_affected_countries)
def showCountryCases():
    selectedCountry = "EG"
    url = "https://api.thevirustracker.com/free-api?countryTotal=" + selectedCountry

    try:
        r = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"

    response = r.text
    data = json.loads(response)
    total_cases=data["results"][0]["total_cases"]
    total_recovered= data["results"][0]["total_recovered"]
    total_deaths= data["results"][0]["total_deaths"]
    total_new_cases_today = data["results"][0]["total_new_cases_today"]
    total_new_deaths_today = data["results"][0]["total_new_deaths_today"]
    total_affected_countries= data["results"][0]["total_affected_countries"]



    return render_template("base 1.html", country_total_cases=total_cases, country_total_recovered=total_recovered,
                           country_total_deaths=total_deaths, country_total_new_cases_today=total_new_cases_today,
                           country_total_new_deaths_today=total_new_deaths_today,
                           country_total_affected_countries=total_affected_countries)

def showAllcountriesCases():
    url = "https://api.thevirustracker.com/free-api?countryTotals=ALL"

    try:
        r = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"

    response = r.text
    data = json.loads(response)
    countryitems = data["countryitems"][0]
    # print(countryitems)

    for i in range(182):
        countrycases =  countryitems[str(i+1)]

        # print(countrycases)
        # print(total_cases)
total_cases = countrycases["total_cases"]
total_recovered = countrycases["total_recovered"]
total_deaths = countrycases["total_deaths"]
total_new_cases_today = countrycases["total_new_cases_today"]
total_new_deaths_today = countrycases["total_new_deaths_today"]


return render_template("base 1.html" ,total_cases=total_cases,total_recovered=total_recovered,total_deaths=total_deaths,
                       total_new_cases_today=total_new_cases_today,total_new_deaths_today=total_new_deaths_today,
                       total_affected_countries=total_affected_countries)

if __name__ == "__main__":
    app.run(debug = True)




print("454649")
showAllcountriesCases()



