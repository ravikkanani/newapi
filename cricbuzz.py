import requests
import json
import sys
from bs4 import BeautifulSoup
from pprint import pprint

r = requests.get('http://mapps.cricbuzz.com/cbzandroid/2.0/currentmatches.json')
data = json.dumps(r.json())
decod=json.loads(data)




class Cricbuzz():


	def matches(self):
		info = decod
		return info

