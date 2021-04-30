import requests
from pprint import pprint
api_key = '' # enter api key you will find from openweathermap.org
city = input("enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)