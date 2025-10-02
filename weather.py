import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

class location:
    def __init__(self, city_name):
        self.city_name = city_name
    
    def get_location_data(self):
        try:
            responce = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.city_name}&limit=1&appid={api_key}")
            self.responce_json = responce.json()
            self.lat = self.responce_json[0]["lat"]
            self.lon = self.responce_json[0]["lon"]
        except:
            print("Fail to get location information.")
            self.lat = None
            self.lon = None
                        
class Weather:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.get_weather_data()

    def get_weather_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={self.lat}&lon={self.lon}&appid={api_key}")
            self.response_json = response.json()
            self.temp = self.response_json["main"]["temp"]
            self.temp_min = self.response_json["main"]["temp_min"]
            self.temp_max = self.response_json["main"]["temp_max"]
            self.humidity = self.response_json["main"]["humidity"]
        except:
            print("Fail to get weather data.")



    def temp_print(self):
        print(f"In {self.name} it is currently {self.temp}° C")
        print(f"Today's High: {self.temp_max}° C")
        print(f"Today's Low: {self.temp_min}° C")
        print(f"Today's Humidity: {self.humidity}%")




city_data = location(input("Which city weather do you want to know?"))
city_data.get_location_data()
city_name = city_data.city_name
city_lat = city_data.lat
city_lon = city_data.lon
my_city = Weather(city_name, city_lat, city_lon)
my_city.temp_print()