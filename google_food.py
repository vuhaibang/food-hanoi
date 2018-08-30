#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=10.779614,%20106.699256&radius=5000&fields=name&keyword=coffee&key=AIzaSyD9kahHndY7IUFgKGWemWF509dfbbNL-Pw

import requests
import json


with open('k.text' ,'r') as f:
	k = f.read()
	

def find_around():
	r = requests.get(k)
	s = json.loads(r.text)
	count = 0
	with open('food.text', 'wt+') as f:
		for i in s['results']:
			count += 1
			f.write(i['name'] + '+' + i['vicinity'] + '\n')
			print(i['name'], i['vicinity'])
		print(count)


find_around()