import json
import requests
#API to fetch temparature of a city
city_name=input("Enter a city name:")
api_key='8d85d06eba28a6c92a52d13aed2bd3a8'
#To build the api url
api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=8d85d06eba28a6c92a52d13aed2bd3a8&units=metric"
get_server_information=requests.get(api_url)
#print(get_server_information.json())
data=(get_server_information.json())
print(data)
pretty_data=json.dumps(data,indent=4)
print(pretty_data)
