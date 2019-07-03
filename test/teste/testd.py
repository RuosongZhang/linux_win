import time
import json
import requests
def _get_access_token():
		url = 'http://www.7timer.info/bin/api.pl?lon=117.585&lat=40.397&product=astro&output=json'

		req = requests.get(url)
		#print(req.json())
		b = req.text)
		c = b.

a = _get_access_token()
print(a)