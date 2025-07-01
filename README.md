# 🌦️ Weather Dashboard

A modern, responsive Django web application that provides comprehensive weather information for any city worldwide using [WeatherAPI.com](https://www.weatherapi.com/). Features a beautiful, dark-mode compatible interface with real-time updates, location-specific timing, and advanced weather alert system.

---

## ✨ Features

### 🔍 **Smart Search & Autocomplete**
- City search with intelligent autocomplete suggestions
- Search by city and country (e.g., `London, United Kingdom`)
- Real-time search suggestions as you type
- Dark-mode compatible autocomplete dropdown

### 🌡️ **Comprehensive Weather Data**
- **Current Weather**: Temperature, feels-like temperature, and weather conditions
- **Detailed Metrics**: Humidity, wind speed, UV index, atmospheric pressure, and dew point
- **Weather Icons**: Dynamic weather condition icons from WeatherAPI
- **Location-Specific Time**: Displays actual local time for the searched city with live updates

### 📊 **Advanced Forecasting**
- **Hourly Forecast**: 24-hour detailed hourly weather predictions with scrollable interface
- **7-Day Forecast**: Complete weekly weather outlook with daily details
- **Detailed Information**: Temperature ranges, weather conditions, rain probability, wind speeds, and UV index

### 🚨 **Weather Alert System**
- **Real-time Alerts**: Integration with WeatherAPI alert system
- **Floating Alert Button**: Positioned at bottom-right with pulsing animation when alerts are active
- **Alert Modal**: Detailed alert information in a styled popup modal
- **Alert Categories**: Severity-based color coding (Severe, Moderate, Minor)
- **Comprehensive Details**: Alert descriptions, instructions, effective/expiry times, and affected areas

### 🎨 **Modern UI/UX**
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Stylish sun/moon toggle switch with persistent preference storage
- **Sectioned Layout**: Clean separation between current weather, hourly, and weekly forecasts in distinct cards
- **Interactive Elements**: Hover effects, smooth transitions, and card animations
- **Beautiful Gradients**: Eye-catching visual design with theme-aware styling
- **Wide Layout**: Optimized for modern wide screens with reduced outer margins

### ⏰ **Real-Time Features**
- **Live Time Updates**: Clock updates every second
- **Location-Aware Time**: Shows actual local time for the searched location
- **Timezone Integration**: Automatic timezone conversion for accurate time display
- **Dynamic Alerts**: Real-time weather alert monitoring and display

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
2. **View Current Weather**: See real-time weather conditions with local time in a beautiful gradient card
3. **Check Hourly Forecast**: Scroll through the next 24 hours of weather predictions in the dedicated hourly section
4. **Plan Ahead**: Review the 7-day weather forecast with detailed daily information
5. **Toggle Dark Mode**: Use the stylish sun/moon switch in the top-right corner for comfortable viewing
6. **Monitor Alerts**: Watch for the floating alert button (bottom-right) when weather alerts are active
7. **View Alert Details**: Click the alert button to see detailed weather warnings and safety instructions

---

## 📱 Responsive Design

The application is fully responsive and optimized for:
- **Desktop**: Full-featured layout with all sections visible in a wide, card-based design
- **Tablet**: Adjusted column layouts for optimal viewing with touch-friendly elements
- **Mobile**: Stacked layout with touch-friendly interface and optimized card spacing
- **Wide Screens**: Enhanced layout for modern ultrawide displays

---

## 🌙 Dark Mode Support

- **Automatic Detection**: Respects system dark mode preference on first visit
- **Stylish Toggle**: Sun/moon icon-based toggle switch with smooth animations
- **Manual Override**: Easy switch to toggle between light and dark themes
- **Persistent Preference**: Remembers your choice across sessions using localStorage
- **Complete Coverage**: All UI elements adapt to the selected theme, including:
  - Weather cards and sections
  - Autocomplete dropdown
  - Alert modals and buttons
  - Section headers with theme-appropriate gradients

---

## 🚨 Weather Alert System

### **Alert Detection**
- Automatic monitoring of weather alerts from WeatherAPI
- Real-time alert status checking with each weather data request
- Support for multiple simultaneous alerts

### **Alert Display**
- **Floating Button**: Positioned at bottom-right corner with pulsing animation
- **Alert Counter**: Badge showing number of active alerts
- **Modal Interface**: Detailed alert information in a responsive modal popup

### **Alert Information**
- **Severity Levels**: Color-coded severity indicators (Severe, Moderate, Minor)
- **Comprehensive Details**: Headlines, descriptions, and safety instructions
- **Time Information**: Effective and expiry times for each alert
- **Geographic Coverage**: Areas and regions affected by the alert
- **Event Categories**: Weather event types and urgency levels

---

## 🔧 Technical Features

### **Backend (Django)**
- Clean, modular code structure with separation of concerns
- Robust error handling and API timeout management
- Efficient weather data processing and parsing
- Timezone-aware datetime handling with location-specific time conversion
- Weather alert integration and data structuring
- RESTful API endpoints for autocomplete functionality

### **Frontend**
- Bootstrap 5 for responsive design and modern components
- Custom CSS with CSS variables for seamless theming
- jQuery UI for enhanced autocomplete with theme-aware styling
- Weather Icons library for beautiful, scalable weather symbols
- Real-time JavaScript updates for time and dynamic content
- Smooth animations and transitions for enhanced user experience
- Modal system for alert management with Bootstrap components

### **Data Sources**
- **WeatherAPI.com**: Reliable weather data with global coverage
- **Current Weather**: Real-time conditions with detailed metrics
- **Forecast Data**: Up to 7 days of weather predictions with hourly breakdowns
- **Alert System**: Real-time weather warnings and safety information
- **Location Services**: Accurate timezone and regional information
- **Autocomplete Data**: City search suggestions with country information

### **Performance Optimizations**
- Efficient API data caching and processing
- Optimized image loading for weather icons
- Minimal JavaScript footprint with targeted updates
- Responsive image sizing for different screen densities
- CSS animations using hardware acceleration

---

## 🎨 UI/UX Design Philosophy

### **Card-Based Layout**
- **Sectioned Design**: Each weather component (current, hourly, weekly) in dedicated cards
- **Visual Hierarchy**: Clear separation and organization of information
- **Consistent Spacing**: Uniform margins and padding throughout the interface

### **Color Scheme**
- **Light Mode**: Clean whites and subtle grays with colorful gradients
- **Dark Mode**: Deep backgrounds with high contrast text for readability
- **Accent Colors**: Weather-appropriate colors for different conditions and alerts

### **Typography**
- **Readable Fonts**: System fonts optimized for web display
- **Hierarchical Text**: Clear distinction between headers, body text, and metadata
- **Responsive Sizing**: Text that scales appropriately across device sizes

### **Interactive Elements**
- **Hover Effects**: Subtle animations on cards and buttons
- **Focus States**: Clear keyboard navigation support
- **Loading States**: Visual feedback during data fetching
- **Error Handling**: User-friendly error messages and fallbacks

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
- `Bootstrap 5.3.0` - CSS framework and component library
- `jQuery 3.7.1` - JavaScript library for DOM manipulation
- `jQuery UI 1.13.3` - UI interactions and autocomplete functionality
- `Weather Icons 2.0.10` - Weather icon fonts and symbols

### **API Integration**
- **WeatherAPI.com** - Primary weather data source
  - Current weather conditions
  - 7-day forecast data
  - Hourly predictions
  - Weather alerts and warnings
  - Location and timezone information

---

## 🚀 Deployment

The application is production-ready and can be deployed to various platforms:

### **Recommended Platforms**
- **Heroku** - Easy deployment with git integration
- **Railway** - Modern platform with automatic deployments
- **Render** - Simple setup with environment variable support
- **PythonAnywhere** - Python-focused hosting with Django support
- **DigitalOcean App Platform** - Scalable cloud deployment

### **Deployment Checklist**
1. Set environment variables (`WEATHERAPI_KEY`, `SECRET_KEY`)
2. Configure static file serving (Whitenoise included)
3. Set `DEBUG=False` in production
4. Configure allowed hosts in Django settings
5. Ensure SSL/HTTPS for secure API calls

### **Environment Variables Required**
```env
WEATHERAPI_KEY=your_weatherapi_key
SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

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

- **[WeatherAPI.com](https://www.weatherapi.com/)** - For providing comprehensive weather data and alert system
- **[Bootstrap](https://getbootstrap.com/)** - For the responsive UI framework and component library
- **[Weather Icons](https://erikflowers.github.io/weather-icons/)** - For beautiful weather iconography
- **[jQuery](https://jquery.com/)** - For enhanced JavaScript functionality and DOM manipulation
- **[jQuery UI](https://jqueryui.com/)** - For autocomplete functionality and UI interactions

---

## � Future Enhancements

### **Planned Features**
- **Map Integration**: Interactive weather maps with radar and satellite imagery
- **Multiple Locations**: Save and track weather for multiple cities
- **Weather History**: Historical weather data and trends
- **Push Notifications**: Browser notifications for severe weather alerts
- **Weather Widgets**: Embeddable weather widgets for other websites
- **API Expansion**: Additional weather data sources for enhanced accuracy

### **Technical Improvements**
- **Progressive Web App (PWA)**: Offline capabilities and app-like experience
- **Caching Strategy**: Redis integration for improved performance
- **Database Integration**: User preferences and location history storage
- **Real-time Updates**: WebSocket integration for live weather updates
- **Internationalization**: Multi-language support for global users

---

## �📧 Support & Contributing

### **Getting Help**
For support, feature requests, or bug reports, please:
1. Check existing issues on GitHub
2. Create a new issue with detailed information
3. Include screenshots for UI-related issues
4. Provide browser and device information for compatibility issues

### **Contributing**
We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Follow the existing code style and conventions
4. Add tests for new functionality
5. Update documentation as needed
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request with a clear description

### **Development Guidelines**
- Follow PEP 8 for Python code style
- Use meaningful variable and function names
- Add comments for complex logic
- Ensure responsive design for all new features
- Test on both light and dark modes
- Maintain accessibility standards

---

## 📄 License

This project is open-source and available under the **MIT License**. Feel free to use, modify, and distribute as needed.

---

**Happy Weather Tracking! 🌤️**

*Stay informed, stay prepared, stay safe with real-time weather insights!*
