import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "N2Aljq21tNwzEZAv2lQAjCP60gCCxe1g"

while True:
   orig = input("Starting Location: ")
   if orig == "quit" or orig == "q":
      break
      
   dest = input("Destination: ")
   if orig == "quit" or orig == "q":
      break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]

   if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
      print("=============================================")
      print("Directions from " + (orig) + " to " + (dest))
      print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
      print("Miles:           " + str(json_data["route"]["distance"]))
      print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
      print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
      print("Fuel Used (Ltr): " + str((json_data["route"]["distance"])*3.78))
      print("=============================================")
