import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Lima, Peru"
dest = "Lince, Peru"
key = "N2Aljq21tNwzEZAv2lQAjCP60gCCxe1g"


url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)