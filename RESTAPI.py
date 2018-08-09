import requests, os
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
print (response.json())

jsonPayload = {'UserId':1, 'title':'test', 'body':'nothing'}
response = requests.post(url,json=jsonPayload)
print(response.json())

url = 'https://jsonplaceholder.typicode.com/posts/51'
response = requests.put(url,json=jsonPayload)
print(response.json())

response = requests.delete(url)
print(response.json()) 

url = 'https://api.github.com/user'
response = requests.get(url,auth=('AdedayoA','b38e3482d6495be984530a46119a969f9acd9eda'))
print(response.json())

my_json = response.json()
for key in my_json.keys():
    print(key)

os.system('clear')

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
my_json = response.json()
url_list = []
for photo in my_json:
    url_list.append(photo['url'])

set(url_list)
print('There were', ( len(url_list) - len(set(url_list)) )  ,'number of duplicates in the json for URLS.')
