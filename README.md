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

### 2. Create and Activate a Virtual Environment

python -m venv venv

    On Windows:

venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

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

### 📄 License

This project is open-source and available under the MIT License.

### 🙌 Acknowledgments

    WeatherAPI.com – for free weather data

    Bootstrap – for responsive UI styling
