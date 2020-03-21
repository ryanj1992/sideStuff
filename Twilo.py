from twilio.rest import Client
import requests
account_sid = 'ACcc2bab9378312d232b3e69d4f7f61d2e'
auth_token = '16c1641dc50691a57ce66ab634e29cf3'

client = Client(account_sid, auth_token)

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"United Kingdom"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "433484533cmsh3673a65341a5a1cp1f1321jsn6f683bad0fbc"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
corona = response.json()

messageString = "The number of cases and deaths in the UK today:\n"

for stats in corona['data']['covid19Stats'][0:1]:
    messageString += "Confirmed Cases: " + str(stats['confirmed']) + "\n"
    messageString += "Deaths: " + str(stats['deaths'])

#formulate the message that will be sent
message = client.messages.create(
    to="+6738649949",
    from_="+12062220354",
    body=messageString)
print(message.sid)
