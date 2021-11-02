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
#    print(json_status)

   if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]) + "Latitud: -12.0833, Longitud: -77.0317")
        print("Millas:           " + str(json_data["route"]["distance"])+ "Latitud: -12.0833, Longitud: -77.0317")
        print("Kilometros:      " + str((json_data["route"]["distance"])*1.61))
        print("Combustible usado (Gal): " + str(json_data["route"]["fuelUsed"])+"Latitud: -12.0833, Longitud: -77.0317")
        print("Combustible usado (Ltr): " + str((json_data["route"]["distance"])*3.78))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+ "("+ str("{:.2f}".format((each["distance"])*1.61)+"km)"))
        print("=============================================")

   elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
   elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
   else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

        
