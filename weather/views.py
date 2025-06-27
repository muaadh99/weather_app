import os
import requests
from django.shortcuts import render
from django.utils import timezone

def get_weather(city="Colombo"):
    api_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            
            # Current weather data
            current_weather = {
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
            
            # 7-day forecast data
            forecast_days = []
            for day in data["forecast"]["forecastday"]:
                # Convert date string to datetime object for proper template formatting
                from datetime import datetime
                date_obj = datetime.strptime(day["date"], "%Y-%m-%d").date()
                
                forecast_days.append({
                    "date": date_obj,  # Pass as date object for template filters
                    "max_temp": day["day"]["maxtemp_c"],
                    "min_temp": day["day"]["mintemp_c"],
                    "condition": day["day"]["condition"]["text"],
                    "icon": day["day"]["condition"]["icon"],
                    "humidity": day["day"]["avghumidity"],
                    "uv": day["day"]["uv"],
                })
            
            return current_weather, forecast_days
    except Exception:
        pass
    return None, None

def index(request):
    city = "Colombo"
    error = ""
    weather = None
    forecast = None
    
    if request.method == "POST":
        city = request.POST.get("city", "Colombo")
    
    weather, forecast = get_weather(city)
    if not weather:
        error = "City not found or API error."
    
    # Add current time for the live clock
    from datetime import datetime
    now = datetime.now()
    
    return render(request, "weather/index.html", {
        "weather": weather, 
        "forecast": forecast,
        "city": city, 
        "error": error,
        "now": now,
    })
