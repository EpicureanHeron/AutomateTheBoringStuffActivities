#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line args

if len(sys.argv) < 2:
    print ('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API

#get your own API KEY! 

apiKey = 'your_api_key'

#Fixed URL from what was on ATBS

url ='http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (location,apiKey)

response = requests.get(url)
response.raise_for_status()

# Load JSON Data 

weatherData = json.loads(response.text)

# Print weather descriptions

w = weatherData['list']

print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
