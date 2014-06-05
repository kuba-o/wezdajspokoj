import requests
import json
from django.http import HttpResponse
import re
#from urllib2 import urlopen

class ArtistParser:

	API_KEY = '93903103571bcd8ca15d664cbe16d6c9'
	API_URL = 'http://ws.audioscrobbler.com/2.0/'

	def download(name):
		parameters = {'method' : 'user.gettopartists', 'user': name, 'api_key': ArtistParser.API_KEY, 'format' : 'json'}
		result = requests.get(ArtistParser.API_URL,params=parameters)
		resultdict = json.loads(result.content.decode("utf-8"))
		response = json.loads(result.content.decode("utf-8"))
		regx=re.compile('<name>(.*)</name>')
		names=regx.findall(str(response))


		#resultdict = json.loads(result.content.decode("utf-8"))
		#regx=re.compile('<name>(.*)</name>') 
		return resultdict.items()
		#return HttpResponse(resultdict)
		#.decode("utf-8")
