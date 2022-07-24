#Source: https://www.tutorialspoint.com/find-current-weather-of-any-city-using-openweathermap-api-in-python

# importing requests and json
import requests, json
import configparser

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

#API Key
config = configparser.ConfigParser()
config.read("Config.ini")
API_KEY = config['API_Key']['Key']

#City Name
CITY = config['Location']['City']

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature, Umrechnung in °C
   temperature = main['temp']-273.15
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   #Transforming the temperature from K into °C
   print(f"{CITY:-^30}")
   #Adding units to output data
   print(f"Temperature: {temperature}" + " °C")
   print(f"Humidity: {humidity}" + " %")
   print(f"Pressure: {pressure}" + " hpa")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")

