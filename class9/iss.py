import requests
import time

URL = 'http://api.open-notify.org/iss-now.json'

j1 = requests.get(URL).json()
time.sleep(10)
j2 = requests.get(URL).json()

timeDiff = abs(int(j2['timestamp']) - int(j1['timestamp']))
latDiff = abs(float(j2['iss_position']['latitude']) - float(j1['iss_position']['latitude']))
longDiff = abs(float(j2['iss_position']['longitude']) - float(j1['iss_position']['longitude']))

print('The ISS has traveled ' + str(latDiff) + ' degrees of latitude and ' + str(longDiff) + ' degrees of longitude in ' + str(timeDiff) + ' seconds.')
