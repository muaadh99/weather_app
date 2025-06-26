import os
import requests
from django.shortcuts import render

def get_weather(city="Colombo"):
    api_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "temp_c": data["current"]["temp_c"],
            "feelslike_c": data["current"]["feelslike_c"],
            "humidity": data["current"]["humidity"],
            "wind_kph": data["current"]["wind_kph"],
            "uv": data["current"]["uv"],
            "pressure_mb": data["current"]["pressure_mb"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
        }
    return None


def index(request):
    weather = get_weather()
    return render(request, "weather/index.html", {"weather": weather})

