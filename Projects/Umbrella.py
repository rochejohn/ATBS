#! python3

import json, requests, sys, pytemperature

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url ='http://api.openweathermap.org/data/2.5/find?q={loc}&APPID=0679f9d4ab90f09aaea8f209b1ce9596'.format(loc=location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.

w = weatherData['list']

# pprint.pprint(w)


weather_output = 'Current weather in {loc}:\n\n'.format(loc=location) + w[0]['weather'][0]['main'] + ' - ' +  w[0]['weather'][0]['description'] +'\n\nCurrent temp is: ' +  str(round(pytemperature.k2c(w[0]['main']['temp']))) +'C' + '\n\nMax temp is: ' +  str(round(pytemperature.k2c(w[0]['main']['temp_max'])))+'C' + '\n\nLowest temp is: ' + str(round(pytemperature.k2c(w[0]['main']['temp_min'])))+'C' + '\n\nThe forcast for rain is: ' +  str(w[0]['rain'])


if w[0]['rain'] == None:
    weather_output += '\n\nLooks like no umbrella is needed today!'

else:
    weather_output += '\n\nYou should bring an umbrella today!'


# Text the weather using Twilio

#This can be used with cron to text every morning to check if umbrella is needed.

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACda2ce57dcdf712414bd13779f3b20331'
auth_token = '1a42f68dd2e333f7513bc6368fd80bdc'
client = Client(account_sid, auth_token)


my_text = weather_output

message = client.messages.create(body=my_text, from_='+61488856205', to='+61435739754')





# Below was the output of json.loads with pprint
# To visualise how to call for data






'''
[{'clouds': {'all': 75},
  'coord': {'lat': 52.2167, 'lon': -8.5834},
  'dt': 1549261800,
  'id': 2964747,
  'main': {'humidity': 87,
           'pressure': 1013,
           'temp': 280.84,
           'temp_max': 281.15,
           'temp_min': 280.15},
  'name': 'Doneraile',
  'rain': None,
  'snow': None,
  'sys': {'country': 'IE'},
  'weather': [{'description': 'broken clouds',
               'icon': '04n',
               'id': 803,
               'main': 'Clouds'}],
  'wind': {'deg': 330, 'speed': 8.2}}]
  '''



















