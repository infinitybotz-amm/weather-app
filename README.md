# Weather Application - Using wttr.in API

A Python weather application that fetches real-time weather data using the **wttr.in API**. Three versions are included: CLI, Simple, and Flask Web Interface.

## 🎯 Features

✅ **Real-time Weather Data** - Get current weather for any city  
✅ **Multiple Interfaces** - CLI, Simple Script, and Web Interface  
✅ **Comprehensive Data** - Temperature, humidity, wind, pressure, and more  
✅ **Error Handling** - Graceful error messages and timeout handling  
✅ **No API Key Required** - Uses free wttr.in API  
✅ **Responsive Design** - Works on mobile, tablet, and desktop  
✅ **Recent Searches** - Stores and displays recent searches locally  
✅ **Location-based** - Get weather for your current location (web version)  

## 📦 Installation

### 1. Clone/Navigate to the weather-app directory

```bash
cd weather-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Python 3.8+ is recommended.

## 🚀 Usage

### Option 1: Simple CLI Script

Quick single weather lookup:

```bash
python3 weather_simple.py
```

Example:
```
Enter city name: London
🌍 Weather in London
Temperature: 15°C (59°F)
Condition: Partly cloudy
Wind Speed: 12 km/h
Humidity: 65%
Feels Like: 13°C
```

### Option 2: Interactive CLI Application

Full-featured terminal interface:

```bash
python3 weather_app.py
```

Menu options:
- Get current weather for a city
- Get weather in plain text
- Exit

### Option 3: Web Interface (Flask)

Start the web server:

```bash
python3 weather_flask_app.py
```

Then visit: **http://localhost:5000**

Features:
- 🔍 Search by city name
- 📍 Get weather for current location
- 📊 Beautiful weather cards with all data
- 💾 Recent searches stored locally
- 📱 Fully responsive design

## 📋 File Structure

```
weather-app/
├── weather_simple.py          # Simple script (minimal version)
├── weather_app.py             # Interactive CLI application
├── weather_flask_app.py       # Flask web server
├── templates/
│   └── weather.html          # Web interface HTML
├── static/
│   ├── style.css             # Web interface styles
│   └── script.js             # Web interface JavaScript
├── requirements.txt          # Python dependencies
├── run_cli.sh               # Run CLI version
├── run_web.sh               # Run web version
└── README.md                # This file
```

## 🔌 API Details

### wttr.in API

**Endpoint:** `https://wttr.in/{city}?format=json`

**Response includes:**
- Current conditions (temperature, humidity, wind speed, etc.)
- Location information (city, country)
- Advanced data (UV index, visibility, pressure, cloudcover)

**No authentication required** - Free to use!

## 📊 Available Weather Data

| Field | Unit | Description |
|-------|------|-------------|
| Temperature | °C / °F | Current temperature |
| Feels Like | °C | Perceived temperature |
| Humidity | % | Relative humidity |
| Wind Speed | km/h | Current wind speed |
| Visibility | km | Visibility distance |
| Pressure | mb | Atmospheric pressure |
| Cloud Cover | % | Cloud coverage percentage |
| Precipitation | mm | Rainfall amount |
| UV Index | - | UV radiation index |

## 🎨 Web Interface Features

### Search
- Type any city name and press Enter or click Search
- Autocomplete suggestions available
- Recent searches stored in browser

### Location
- Click "📍 Current Location" button
- Grant permission to share your location
- See weather for your current position

### Weather Display
- Large temperature display with °C and °F
- Condition description with emoji
- Detailed weather cards for all parameters
- Progress bars for humidity and cloud cover
- Last updated timestamp

### Responsive Design
- Desktop view: 2-3 columns
- Tablet view: 2 columns
- Mobile view: 1 column
- Touch-friendly buttons

## ⚙️ Configuration

### Timeout Settings

Modify request timeout in `weather_app.py`:

```python
response = self.session.get(url, timeout=10)  # 10 seconds
```

### API Format

Available formats from wttr.in:
- `json` - JSON response
- `text` - Plain text format
- `png` - Image (ASCII art)

## 🐛 Troubleshooting

### "City not found" error
- Check city name spelling
- Try English name (not local language)
- Try with country code: "London, UK"

### "Request timeout" error
- Check internet connection
- Try again in a few moments
- wttr.in servers might be overloaded

### Flask app won't start
- Make sure port 5000 is not in use
- Try: `python3 weather_flask_app.py`
- Install Flask: `pip install Flask`

### No recent searches showing
- Enable browser local storage
- Check if JavaScript is enabled
- Clear browser cache if needed

## 📚 Code Examples

### Fetch weather programmatically

```python
from weather_app import WeatherApp

app = WeatherApp()
weather = app.get_weather_json("Paris")

if weather:
    current = weather['current_condition'][0]
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Condition: {current['weatherDesc'][0]['value']}")
```

### Use weather service in your code

```python
from weather_flask_app import WeatherService

data = WeatherService.get_weather("Tokyo")
parsed = WeatherService.parse_weather(data)

if parsed:
    print(f"Weather in {parsed['city']}: {parsed['temperature']}°C")
```

### Make API request with requests library

```python
import requests

response = requests.get("https://wttr.in/London?format=json")
weather = response.json()

print(weather['current_condition'][0]['temp_C'])
```

## 🔒 Privacy

- Web version stores searches locally in browser
- No data sent to external servers (except wttr.in for weather)
- No tracking or analytics
- Geolocation only used when you explicitly click the button
- All processing done on your device

## 📖 Additional Resources

- **wttr.in Documentation:** https://wttr.in/:help
- **wttr.in GitHub:** https://github.com/chubin/wttr.in
- **Requests Library:** https://requests.readthedocs.io/
- **Flask Documentation:** https://flask.palletsprojects.com/

## 🤝 Contribute

Feel free to enhance the app:
- Add more weather parameters
- Implement weather forecasts
- Add multiple city comparison
- Create mobile app
- Add more language support

## 📝 License

Free to use and modify for personal or educational purposes.

## 🙋 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify internet connection
3. Try a different city
4. Check wttr.in service status

---

**Enjoy checking the weather! 🌤️**
