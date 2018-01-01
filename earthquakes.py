import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)


    # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print (i["properties"]["title"])

      # print the events that only have a magnitude greater than 4
#  for i in theJSON["features"]:
#    if i["properties"]["mag"] >= 4.0:
#      print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

      # print only the events where at least 1 person reported feeling something
 # print ("Events that were felt:")
 # for i in theJSON["features"]:
 #   feltReports = i["properties"]["felt"]
 #   if (feltReports != None):
 #     if (feltReports > 0):
  #      print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")

def user_input_number_EQ():
  user_input = input("What magnitude of earthquakes would you like to view:\n1) All Magnitudes\n2) 1.0 Magnitude \n3) 2.5 Magnitude\n4) 4.5 Magnitude \n5) Significant Magnitude\n")
  return user_input

def menu():
  url = ""
  user_input = input("Would you like to view earthquakes from the past:\n1) Hour\n2) Day \n3) 7 Days\n4) 30 Days\n")
  if (user_input == '1'):
    user_input2 = user_input_number_EQ()
    if (user_input2 == '1'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    elif (user_input2 == '2'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
    elif (user_input2 == '3'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    elif (user_input2 == '4'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"
    elif (user_input2 == '5'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"
  elif (user_input == '2'):
    user_input2 = user_input_number_EQ()
    if (user_input2 == '1'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    elif (user_input2 == '2'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"
    elif (user_input2 == '3'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    elif (user_input2 == '4'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    elif (user_input2 == '5'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson"
  elif (user_input == '3'):
    user_input2 = user_input_number_EQ()
    if (user_input2 == '1'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
    elif (user_input2 == '2'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson"
    elif (user_input2 == '3'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"
    elif (user_input2 == '4'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
    elif (user_input2 == '5'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson"
  elif (user_input == '4'):
    user_input2 = user_input_number_EQ()
    if (user_input2 == '1'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    elif (user_input2 == '2'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
    elif (user_input2 == '3'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
    elif (user_input2 == '4'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
    elif (user_input2 == '5'):
      url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
  return url

def main():
  urlData = menu()

    # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    data = data.decode("utf-8") 
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
  main()
