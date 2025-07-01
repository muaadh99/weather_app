# 🌦️ Weather Dashboard

A modern, responsive Django web application that provides comprehensive weather information for any city worldwide using [WeatherAPI.com](https://www.weatherapi.com/). Features a beautiful, dark-mode compatible interface with real-time updates and location-specific timing.

---

## ✨ Features

### 🔍 **Smart Search & Autocomplete**
- City search with intelligent autocomplete suggestions
- Search by city and country (e.g., `London, United Kingdom`)
- Real-time search suggestions as you type

### 🌡️ **Comprehensive Weather Data**
- **Current Weather**: Temperature, feels-like temperature, and weather conditions
- **Detailed Metrics**: Humidity, wind speed, UV index, atmospheric pressure, and dew point
- **Weather Icons**: Dynamic weather condition icons
- **Location-Specific Time**: Displays actual local time for the searched city

### 📊 **Advanced Forecasting**
- **Hourly Forecast**: 24-hour detailed hourly weather predictions
- **7-Day Forecast**: Complete weekly weather outlook
- **Detailed Information**: Temperature ranges, weather conditions, rain probability, and wind speeds

### 🎨 **Modern UI/UX**
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Dark/Light Mode**: Toggle between themes with persistent preference storage
- **Sectioned Layout**: Clean separation between current weather, hourly, and weekly forecasts
- **Interactive Elements**: Hover effects and smooth transitions
- **Beautiful Gradients**: Eye-catching visual design with modern styling

### ⏰ **Real-Time Features**
- **Live Time Updates**: Clock updates every second
- **Location-Aware Time**: Shows actual local time for the searched location
- **Timezone Integration**: Automatic timezone conversion for accurate time display

---

## 🛠️ Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **A free [WeatherAPI.com](https://www.weatherapi.com/) API key**

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/muaadh99/weather_app.git
cd weather_app
```

### 2. Create and Activate a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the project root (same level as `manage.py`) and add:

```env
WEATHERAPI_KEY=your_actual_api_key_here
SECRET_KEY=your_django_secret_key_here
```

**To get your WeatherAPI key:**
1. Visit [WeatherAPI.com](https://www.weatherapi.com/)
2. Sign up for a free account
3. Copy your API key from the dashboard

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

**Access the application:**
Open your browser and visit: `http://127.0.0.1:8000/`

---

## 🎯 Usage

1. **Search for a City**: Type any city name in the search box (e.g., "Tokyo, Japan")
2. **View Current Weather**: See real-time weather conditions with local time
3. **Check Hourly Forecast**: Scroll through the next 24 hours of weather predictions
4. **Plan Ahead**: Review the 7-day weather forecast
5. **Toggle Dark Mode**: Use the switch in the top-right corner for comfortable viewing

---

## 📱 Responsive Design

The application is fully responsive and optimized for:
- **Desktop**: Full-featured layout with all sections visible
- **Tablet**: Adjusted column layouts for optimal viewing
- **Mobile**: Stacked layout with touch-friendly interface

---

## 🌙 Dark Mode Support

- **Automatic Detection**: Respects system dark mode preference
- **Manual Toggle**: Easy switch to toggle between light and dark themes
- **Persistent Preference**: Remembers your choice across sessions
- **Complete Coverage**: All UI elements, including autocomplete suggestions, adapt to the selected theme

---

## 🔧 Technical Features

### **Backend (Django)**
- Clean, modular code structure
- Robust error handling
- Efficient API data processing
- Timezone-aware datetime handling

### **Frontend**
- Bootstrap 5 for responsive design
- Custom CSS with CSS variables for theming
- jQuery UI for enhanced autocomplete
- Weather Icons library for beautiful weather symbols
- Real-time JavaScript updates

### **Data Sources**
- **WeatherAPI.com**: Reliable weather data with global coverage
- **Location Services**: Accurate timezone and regional information
- **Forecast Data**: Up to 7 days of weather predictions

---

## 📦 Dependencies

### **Core Dependencies**
- `Django 5.2.3` - Web framework
- `requests 2.32.4` - HTTP library for API calls
- `python-dotenv 1.1.1` - Environment variable management

### **Production Dependencies**
- `gunicorn 23.0.0` - WSGI HTTP Server
- `whitenoise 6.9.0` - Static file serving

### **Frontend Libraries**
- `Bootstrap 5.3.0` - CSS framework
- `jQuery 3.7.1` - JavaScript library
- `jQuery UI 1.13.3` - UI interactions
- `Weather Icons 2.0.10` - Weather icon fonts

---

## 🚀 Deployment

The application is production-ready and can be deployed to platforms like:
- **Heroku**
- **Railway**
- **Render**
- **PythonAnywhere**
- **DigitalOcean**

Ensure environment variables are properly configured in your deployment platform.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Acknowledgments

- **[WeatherAPI.com](https://www.weatherapi.com/)** - For providing comprehensive weather data
- **[Bootstrap](https://getbootstrap.com/)** - For the responsive UI framework
- **[Weather Icons](https://erikflowers.github.io/weather-icons/)** - For beautiful weather iconography
- **[jQuery](https://jquery.com/)** - For enhanced JavaScript functionality

---

## 📧 Support

For support, feature requests, or bug reports, please open an issue on the GitHub repository.

**Happy Weather Tracking! 🌤️**
