# 🌦️ Weather App

A simple Django web application to display current weather information for any city using [WeatherAPI.com](https://www.weatherapi.com/).

---

## ✨ Features

- 🔍 Search weather by city and country (e.g., `Galle, Sri Lanka`)
- 💡 Responsive Bootstrap UI
- 📊 Displays:
  - Temperature  
  - Humidity  
  - Wind Speed  
  - UV Index  
  - Atmospheric Pressure  
  - Weather Condition & Icons

---

## 🛠️ Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- A free [WeatherAPI.com](https://www.weatherapi.com/) API key

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/muaadh99/weather_app.git
cd weather_app
```

### 4. Add Your WeatherAPI Key

- Create a file named `.env` in the project root (same level as `manage.py`)
- Add the following line (replace with your actual API key):

WEATHERAPI_KEY=your_actual_api_key


---

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

python manage.py runserver

Then open your browser and visit:

http://127.0.0.1:8000/

Search for a city (e.g., Galle, Sri Lanka) to view the weather report.

### 📁 Project Structure

weather_app/
├── venv/                     # Virtual environment (not tracked by Git)
├── weather_reporter/         # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather/                  # Django app for weather features
│   ├── migrations/
│   ├── templates/
│   │   └── weather/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .env                      # Environment variables (not tracked by Git)
├── .gitignore                # Specifies untracked files to ignore
├── manage.py                 # Django’s command-line utility
└── requirements.txt          # Python dependencies
