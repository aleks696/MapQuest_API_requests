import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "GUXHPses49aT2eCjM8j2MVOjM9UPJadh" #Input your own API Key

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    route = input("Do you want to choose route type? Y/N: ")
    if route == "Y":
        routeType = input("Fastest = Fastest, Shortest = Shortest, Pedestrian = Pedestrian, Bicycle = Bicycle: ")
        if routeType == "Fastest":
            routeType == "FASTEST"
        if routeType == "Shortest":
            routeType == "SHORTEST"
        if routeType == "Pedestrian":
            routeType == "PEDESTRIAN"
        if routeType == "Bicycle":
            routeType == "BICYCLE"
    else:
        routeType = "FASTEST"
    if route== "quit" or route == "q":
        break

    collections = "check"
    narrat = input("Show narratives? Y/N: ")
    if narrat == "quit" or narrat == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest, "routeType":routeType, "ambiguities": collections})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Start point: " + (json_data["route"]["locations"][0]["adminArea4"]))
        print("End point: " + (json_data["route"]["locations"][1]["adminArea4"]))
        print("=============================================")
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Rote Type: " + (json_data["route"]["options"]["routeType"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        
        if narrat == "Y": 
            for i in json_data["route"]["legs"][0]["maneuvers"]:
                print((i["narrative"]) + " (" + str("{:.2f}".format((i["distance"])*1.61) + " km)"))
                print("Go for " + (i["formattedTime"]) + " h by " + (i["transportMode"]))
            print("=============================================\n")
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
