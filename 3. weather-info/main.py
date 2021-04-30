import requests
from pprint import pprint
<<<<<<< HEAD
api_key = '' # enter api key you will find from openweathermap.org
=======
api_key = '' #enter api key
>>>>>>> 07701a7b1cd3cdb01d7fe154be6d6dff7d12d16f
city = input("enter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
weather_data = requests.get(base_url).json()
pprint(weather_data)
<<<<<<< HEAD



=======
>>>>>>> 07701a7b1cd3cdb01d7fe154be6d6dff7d12d16f
