import requests
from pprint import pprint
api_key = 'b69dffbeebf9d1827f468302f7c76eb4'
city = input("enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)
a = input('\npress enter to exit')


