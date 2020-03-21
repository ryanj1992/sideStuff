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

messageString = ""

for stats in corona['data']['covid19Stats'][0:1]:
    messageString += "Confirmed Cases: " + str(stats['confirmed'])
    messageString += "Deaths: " + str(stats['deaths'])

message = client.messages.create(
    to="+6738649949",
    from_="+12062220354",
    body=messageString)
print(message.sid)