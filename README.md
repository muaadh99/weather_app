## Weather App

A simple Django web application to display current weather information for any city using WeatherAPI.com.
Features

    Search weather by city and country (e.g., Galle, Sri Lanka)

    Responsive Bootstrap UI

    Displays temperature, humidity, wind speed, UV index, pressure, and more

## Prerequisites

    Python 3.8+

    pip

    A free WeatherAPI.com API key

## Setup Instructions

    Clone the repository

bash
git clone https://github.com/muaadh99/weather_app.git
cd weather_app

## Create and activate a virtual environment

bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

## Install dependencies

bash
pip install -r requirements.txt

## Add your WeatherAPI key to a .env file

    Create a file named .env in the project root (same level as manage.py)

    Add this line (replace with your actual API key):

    WEATHERAPI_KEY=your_actual_api_key

## Apply migrations

bash
python manage.py migrate

## Run the development server

    bash
    python manage.py runserver

    Open in your browser

        Visit http://127.0.0.1:8000/

        Search for a city (e.g., Galle, Sri Lanka)

## Project Structure

weather_app/
├── venv/
├── weather_reporter/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather/
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
├── .env
├── .gitignore
├── manage.py
└── requirements.txt