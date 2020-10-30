from twilio.rest import Client
import requests
account_sid = '*******'
auth_token = '*******'

client = Client(account_sid, auth_token)

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"United Kingdom"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "********"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
corona = response.json()

messageString = "The amount of cases and deaths in the UK today:\n"

for stats in corona['data']['covid19Stats'][0:1]:
    messageString += "Confirmed Cases: " + str(stats['confirmed']) + "\n"
    messageString += "Deaths: " + str(stats['deaths'])

#formulate the message that will be sent
message = client.messages.create(
    to="******",
    from_="*******",
    body=messageString)
print(message.sid)
