import requests
import json

result = []
with open('face.text','r') as f:
	access_token = f.read()


def find(key, distance, location,types, token):
	with open('quanan.text', 'wt') as f:
		for k in key:
			url = 'https://graph.facebook.com/v3.1/'
			web = 'search?q={}&type={}&center={}&distance={}&fields=name,location,website&access_token={}'.format(k, types, location, distance, token)
			r = requests.get(url + web)
			s = json.loads(r.text)
			try:
				for n in s['data']:
					for h in tag:
						a = n['name'].lower()
						if h in a:
							f.write((n['name'] + ' ' + n['location']['street'] + '\n'))
							break
				
			except:
				pass
			while 'next' in s['paging']:
				r = requests.get(s['paging']['next'])
				s = json.loads(r.text)
				try:
					for n in s['data']:
						for h in tag:
							a = n['name'].lower()
							if h in a:
								f.write((n['name'] + ' ' + n['location']['street'] + '\n'))
								break			
				except:
					pass
            	
	

tag = ['cơm', 'phở', 'lẩu', 'vịt']
find(tag, '3000', '20.968419,105.7787715', 'place', access_token)