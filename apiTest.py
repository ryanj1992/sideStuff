import requests
from twilio.rest import Client

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"United Kingdom"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "433484533cmsh3673a65341a5a1cp1f1321jsn6f683bad0fbc"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
corona = response.json()
messageString = querystring['country'] + "\n"

for stats in corona['data']['covid19Stats'][0:1]:
    messageString += "Confirmed Cases: " + str(stats['confirmed']) + "\n"
    messageString += "Deaths: " + str(stats['deaths']) + "\n"
    messageString += "Last Update: " + str(stats['lastUpdate'])

print(messageString)