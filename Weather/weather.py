#X0uyORvMmu25IBAJJQJKa8du4Dcf824G <-- API Key
import requests, os, json, webbrowser
def nameOfCity():
	user_input = input("Please enter your city name: ")
	return user_input

def zipOfCity():
	user_input = input("Please enter your zip code: ")
	return user_input



name_of_cities =  nameOfCity()
url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=X0uyORvMmu25IBAJJQJKa8du4Dcf824G&q={}".format( name_of_cities )
#url2 = "http://dataservice.accuweather.com/currentconditions/v1/{}?apikey=X0uyORvMmu25IBAJJQJKa8du4Dcf824G".format( location )
response = requests.get(url)
my_json = response.json()


i=1
for key in my_json:
	print(i , key["LocalizedName"] + ", " + key["Country"]["LocalizedName"])
	print(key["AdministrativeArea"]["LocalizedName"] + ", " + key["PrimaryPostalCode"])
	print("")
	i+=1

def find_zip(proper_city):
	proper_location = ""
	for key in my_json:
		if (key["PrimaryPostalCode"] == proper_city):
			proper_location = key["Key"]
	return proper_location


zip_code = zipOfCity()
location = find_zip(zip_code)

url2 = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{}?apikey=X0uyORvMmu25IBAJJQJKa8du4Dcf824G".format( location )
response2 = requests.get(url2)
my_json2 = response2.json()

for key in my_json2:
	print("At " + key["DateTime"][11:16])
	print("Right now the weather will be " + key["IconPhrase"] )
	print("The temperature will be " , key["Temperature"]["Value"], key["Temperature"]["Unit"])
	print("")
	#webbrowser.open(key["Link"])
