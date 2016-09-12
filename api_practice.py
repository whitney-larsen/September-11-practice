from urllib2 import urlopen
from json import load

apiUrl = "https://data.sfgov.org/resource/6a9r-agq8.json?applicant=JapaCurry"
response = urlopen(apiUrl)
json_obj = load(response)

print type(json_obj)

for i in range(len(json_obj)):
	print json_obj[i]["fooditems"]