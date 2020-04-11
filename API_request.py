
import json
import urllib2
import pandas as pd

def data(query):
    if query is "summary":
        url = "https://api.covid19api.com/summary"
        json_object = urllib2.urlopen(url)
        data = json.load(json_object)
        Global_status = data["Global"]
        df_global = pd.DataFrame.from_dict(Global_status, orient="index")
        print(df_global)
        countries_status = data["Countries"]
        for i in range(len(countries_status)):
            df_countries = pd.DataFrame.from_dict(countries_status[i], orient="index")
            print(df_countries)

    elif query is "country":
        country = input("Enter your country name in small characters between\"\":")
        url = "https://api.covid19api.com/live/country/"+country+"/status/confirmed"
        json_object = urllib2.urlopen(url)
        data_country = json.load(json_object)
        for i in range(len(data_country)):
            df_country = pd.DataFrame.from_dict(data_country[i], orient="index")
            print(df_country)

data("country")
# data("summary")
