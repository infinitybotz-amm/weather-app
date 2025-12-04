# Weather App - Quick Start Guide

## 🚀 Quick Setup (2 minutes)

### Step 1: Install Dependencies

```bash
cd /Users/dhruvika/Documents/Workspace/weather-app
pip install -r requirements.txt
```

### Step 2: Choose Your Interface

#### 🖥️ Simple CLI (One-time lookup)
```bash
python3 weather_simple.py
```
Enter a city name → Get instant weather data

#### 💻 Interactive CLI (Full featured)
```bash
python3 weather_app.py
```
Menu-driven interface with multiple options

#### 🌐 Web Interface (Beautiful UI)
```bash
python3 weather_flask_app.py
```
Visit: http://localhost:5000

## 📝 Examples

### Example 1: Quick Weather Check
```bash
$ python3 weather_simple.py
Enter city name: London
🌍 Weather in London
Temperature: 15°C (59°F)
Condition: Partly cloudy
Wind Speed: 12 km/h
Humidity: 65%
Feels Like: 13°C
```

### Example 2: Using in Python Code
```python
from weather_app import WeatherApp

app = WeatherApp()
app.display_current_weather("Paris")
```

### Example 3: Get JSON Data
```python
import requests

response = requests.get("https://wttr.in/Tokyo?format=json")
data = response.json()
print(data['current_condition'][0]['temp_C'])
```

## 🔥 Features Overview

| Feature | CLI Simple | CLI Full | Web Interface |
|---------|-----------|----------|---------------|
| City Search | ✅ | ✅ | ✅ |
| Current Weather | ✅ | ✅ | ✅ |
| Temperature | ✅ | ✅ | ✅ |
| Humidity/Wind | ✅ | ✅ | ✅ |
| Multiple Formats | ❌ | ✅ | ✅ |
| Recent Searches | ❌ | ❌ | ✅ |
| Location-based | ❌ | ❌ | ✅ |
| Responsive Design | ❌ | ❌ | ✅ |

## 🎯 What to Try First

1. **Quick Test**
   ```bash
   python3 weather_simple.py
   ```
   Input: `London` → See instant weather

2. **Interactive Mode**
   ```bash
   python3 weather_app.py
   ```
   Choose option 1 → Enter city → See formatted data

3. **Web Interface**
   ```bash
   python3 weather_flask_app.py
   ```
   Open http://localhost:5000 → Search for cities

## 📊 Sample Output

### CLI Output
```
==================================================
📍 Weather in NEW YORK
==================================================
🌡️  Temperature: 22°C (72°F)
💨 Wind Speed: 15 km/h
💧 Humidity: 55%
👁️  Visibility: 10 km
🌫️  Pressure: 1013 mb
☁️  Cloud Cover: 40%
📝 Weather: Sunny
🌧️  Precipitation: 0 mm
💦 Feels Like: 20°C
==================================================
```

### Web Interface Displays
- Current temperature with real feel
- Comprehensive weather cards
- Humidity and cloud cover bars
- Wind, pressure, visibility data
- UV index and precipitation
- Recent search history
- Current location weather

## 🔗 API Info

Using **wttr.in** - Free public weather API
- No API key needed
- Accurate data from weather services
- Supports 15,000+ cities
- Works worldwide

## ✅ Verification

Test if everything works:

```bash
# Test 1: Check Python
python3 --version

# Test 2: Check requests library
python3 -c "import requests; print('✅ Requests OK')"

# Test 3: Test API
curl "https://wttr.in/London?format=json" | head -20

# Test 4: Run simple script
python3 weather_simple.py
```

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module named requests" | Run: `pip install requests` |
| "City not found" | Try English name or "City, Country" |
| "Request timeout" | Check internet, try again |
| Flask port 5000 busy | Change port in weather_flask_app.py |
| Location not working (web) | Check browser permissions |

## 📚 Files Reference

| File | Purpose | Run Command |
|------|---------|------------|
| `weather_simple.py` | Single weather lookup | `python3 weather_simple.py` |
| `weather_app.py` | Interactive CLI app | `python3 weather_app.py` |
| `weather_flask_app.py` | Web interface | `python3 weather_flask_app.py` |
| `templates/weather.html` | Web UI template | Part of Flask app |
| `static/style.css` | Web styling | Part of Flask app |
| `static/script.js` | Web functionality | Part of Flask app |

## 🎓 Learn More

- Study `weather_app.py` for full error handling
- Check `weather_flask_app.py` for API integration
- Explore `static/script.js` for frontend logic
- Read wttr.in API at: https://wttr.in/:help

## ✨ Next Steps

1. ✅ Install and test one version
2. ✅ Try searching for different cities
3. ✅ Explore the web interface if interested
4. ✅ Integrate into your own projects

---

**Happy weather tracking! 🌤️**
