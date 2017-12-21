# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import os
# TODO: replace with your own app_id and app_key
app_id = 'f71b63b4'
app_key = '40fe87f2d28640b967d54bbe346a37ab'

language = 'en'
word_id = raw_input("Enter in a word: ")

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/sentences'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

j = r.json()
os.system('clear')
counter1 = 0 
counter2 = 0 

print "Example sentences of " + word_id + ' as a ' + j['results'][0]['lexicalEntries'][0]['lexicalCategory']
while counter1 < 5:
	print str(counter1+1) +') ' + j['results'][0]['lexicalEntries'][0]['sentences'][counter1]['text'] + '\n'
	counter1 += 1

"""print "Example sentences of " + word_id + ' as a ' + j['results'][0]['lexicalEntries'][1]['lexicalCategory']
while counter2 < 5:
	print str(counter1+1) +') ' + j['results'][0]['lexicalEntries'][1]['sentences'][counter2]['text'] + '\n'
	counter2 += 1
"""