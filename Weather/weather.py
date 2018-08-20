#X0uyORvMmu25IBAJJQJKa8du4Dcf824G <-- API Key
import requests, os, json
def numOfCity():
	user_input = int(input("How many cities do you want to display?\nEnter 50 | 100 | 150: "))
	if user_input == 50 or user_input == 100 or user_input == 150:
		return user_input
	else:
		print("Error, please enter 50, 100, or 150")
		user_input = input("How many cities do you want to display?\nEnter 50 | 100 | 150: ")
	return user_input

number_of_cities =  numOfCity()
url = "http://dataservice.accuweather.com/currentconditions/v1/topcities/{}?apikey=X0uyORvMmu25IBAJJQJKa8du4Dcf824G".format( number_of_cities )
response = requests.get(url)
my_json = response.json()


i=1
for key in my_json:
	print(i , key["LocalizedName"])
	i+=1

