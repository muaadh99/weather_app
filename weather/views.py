import os
import requests
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime


def get_weather(city="Colombo"):
    api_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7&aqi=no&alerts=yes"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            
            # Parse location local time
            location_localtime = None
            if "localtime" in data["location"]:
                try:
                    location_localtime = datetime.strptime(data["location"]["localtime"], "%Y-%m-%d %H:%M")
                except:
                    location_localtime = None
            
            # Current weather data
            current_weather = {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "region": data["location"]["region"],
                "localtime": location_localtime,
                "timezone_id": data["location"]["tz_id"],
                "temp_c": data["current"]["temp_c"],
                "feelslike_c": data["current"]["feelslike_c"],
                "humidity": data["current"]["humidity"],
                "wind_kph": data["current"]["wind_kph"],
                "uv": data["current"]["uv"],
                "pressure_mb": data["current"]["pressure_mb"],
                "condition": data["current"]["condition"]["text"],
                "dewpoint_c": data["current"].get("dewpoint_c"),
                "icon": data["current"]["condition"]["icon"],
                "last_updated": data["current"]["last_updated"],
            }
            
            # 7-day forecast data
            forecast_days = []
            for day in data["forecast"]["forecastday"]:
                date_obj = datetime.strptime(day["date"], "%Y-%m-%d").date()
                forecast_days.append({
                    "date": date_obj,
                    "max_temp": day["day"]["maxtemp_c"],
                    "min_temp": day["day"]["mintemp_c"],
                    "condition": day["day"]["condition"]["text"],
                    "icon": day["day"]["condition"]["icon"],
                    "humidity": day["day"]["avghumidity"],
                    "uv": day["day"]["uv"],
                })
            
            # Today's hourly forecast (24 hours)
            hourly_forecast = []
            if data["forecast"]["forecastday"]:
                for hour in data["forecast"]["forecastday"][0]["hour"]:
                    hour_time = datetime.strptime(hour["time"], "%Y-%m-%d %H:%M")
                    hourly_forecast.append({
                        "time": hour_time,
                        "temp_c": hour["temp_c"],
                        "condition": hour["condition"]["text"],
                        "icon": hour["condition"]["icon"],
                        "chance_of_rain": hour["chance_of_rain"],
                        "humidity": hour["humidity"],
                        "wind_kph": hour["wind_kph"],
                        "feelslike_c": hour["feelslike_c"],
                    })
            
            # Weather alerts
            alerts = []
            if "alerts" in data and "alert" in data["alerts"]:
                for alert in data["alerts"]["alert"]:
                    alerts.append({
                        "headline": alert.get("headline", "Weather Alert"),
                        "msgtype": alert.get("msgtype", ""),
                        "severity": alert.get("severity", ""),
                        "urgency": alert.get("urgency", ""),
                        "areas": alert.get("areas", ""),
                        "category": alert.get("category", ""),
                        "certainty": alert.get("certainty", ""),
                        "event": alert.get("event", ""),
                        "note": alert.get("note", ""),
                        "effective": alert.get("effective", ""),
                        "expires": alert.get("expires", ""),
                        "desc": alert.get("desc", ""),
                        "instruction": alert.get("instruction", ""),
                    })
            
            return current_weather, forecast_days, hourly_forecast, alerts
    except Exception:
        pass
    return None, None, None, None



def city_autocomplete(request):
    api_key = os.getenv("WEATHERAPI_KEY")
    query = request.GET.get("term", "")
    if not query:
        return JsonResponse([], safe=False)
    url = f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={query}"
    resp = requests.get(url)
    if resp.status_code == 200:
        results = resp.json()
        suggestions = [f"{loc['name']}, {loc['country']}" for loc in results]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

def index(request):
    city = "Colombo"
    error = ""
    weather = None
    forecast = None
    
    if request.method == "POST":
        city = request.POST.get("city", "Colombo")
    
    weather, forecast, hourly, alerts = get_weather(city)
    if not weather:
        error = "City not found or API error."
    
    now = datetime.now()
    
    return render(request, "weather/index.html", {
        "weather": weather, 
        "forecast": forecast,
        "hourly": hourly,
        "alerts": alerts,
        "city": city, 
        "error": error,
        "now": now,
    })

