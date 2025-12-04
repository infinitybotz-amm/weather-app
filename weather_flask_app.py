"""
Advanced Weather Application with Flask Web Interface
Fetch and display weather data with a web UI
"""

from flask import Flask, render_template, request, jsonify
import requests
import json
from datetime import datetime


app = Flask(__name__)


class WeatherService:
    """Weather service class"""
    
    BASE_URL = "https://wttr.in"
    
    @staticmethod
    def get_weather(city):
        """Fetch weather data from wttr.in API"""
        try:
            url = f"{WeatherService.BASE_URL}/{city}?format=j1"
            response = requests.get(url, timeout=15)
            
            # Check if response is valid
            if response.status_code == 404:
                return {"error": "City not found"}
            elif response.status_code != 200:
                return {"error": f"API Error: {response.status_code}"}
            
            # Try to parse JSON
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"error": "Invalid response from API"}
                
        except requests.exceptions.ConnectTimeout:
            return {"error": "Connection timeout - check internet"}
        except requests.exceptions.ReadTimeout:
            return {"error": "Request timeout - try again"}
        except requests.exceptions.ConnectionError:
            return {"error": "No internet connection"}
        except Exception as e:
            return {"error": f"Error: {str(e)}"}

    # Simple static suggestions mapping for popular cities.
    # This is intentionally local and lightweight. We can later replace with a Places API if desired.
    SUGGESTIONS = {
        'london': [
            {'name': 'British Museum', 'desc': 'World-famous museum of human history and culture.', 'category': 'museum'},
            {'name': 'Tower of London', 'desc': 'Historic castle and former prison on the Thames.', 'category': 'historic'},
            {'name': 'Covent Garden', 'desc': 'Lively area with shops, street performers and market.', 'category': 'market'},
            {'name': 'Hyde Park', 'desc': 'Large park ideal for walks and boating.', 'category': 'park'},
            {'name': 'The Shard', 'desc': 'Skyscraper with panoramic city views.', 'category': 'viewpoint'},
            {'name': 'Camden Market', 'desc': 'Eclectic market with food, fashion and crafts.', 'category': 'market'},
        ],
        'mumbai': [
            {'name': 'Gateway of India', 'desc': 'Iconic arch facing the Arabian Sea.', 'category': 'historic'},
            {'name': 'Colaba Causeway', 'desc': 'Bustling street market popular with visitors.', 'category': 'market'},
            {'name': 'Chhatrapati Shivaji Maharaj Terminus', 'desc': 'Historic UNESCO site and architectural marvel.', 'category': 'historic'},
            {'name': 'Marine Drive', 'desc': 'Scenic boulevard along the coast at sunset.', 'category': 'viewpoint'},
            {'name': 'Haji Ali Dargah', 'desc': 'Sacred mosque and tomb on an islet.', 'category': 'religious'},
        ],
        'paris': [
            {'name': 'Eiffel Tower', 'desc': 'World-famous iron tower with observation decks.', 'category': 'viewpoint'},
            {'name': 'Louvre Museum', 'desc': 'Largest art museum with the Mona Lisa.', 'category': 'museum'},
            {'name': 'Montmartre', 'desc': 'Historic artists district with Sacré-Cœur.', 'category': 'neighborhood'},
        ],
        'new york': [
            {'name': 'Central Park', 'desc': 'Large urban park with lakes and trails.', 'category': 'park'},
            {'name': 'Statue of Liberty', 'desc': 'Iconic symbol of freedom on Liberty Island.', 'category': 'historic'},
            {'name': 'Times Square', 'desc': 'Busy commercial intersection and entertainment hub.', 'category': 'neighborhood'},
        ],
        'tokyo': [
            {'name': 'Sensō-ji Temple', 'desc': 'Ancient Buddhist temple in Asakusa.', 'category': 'temple'},
            {'name': 'Shibuya Crossing', 'desc': 'Famous busy intersection and shopping area.', 'category': 'landmark'},
            {'name': 'Meiji Shrine', 'desc': 'Shinto shrine set in a large forested area.', 'category': 'religious'},
        ],
    }

    @staticmethod
    def get_suggestions(city):
        """Return a small list of suggested places to visit for a city.

        This uses a static mapping and falls back to generic suggestions if city not in map.
        """
        if not city:
            return []
        key = city.strip().lower()
        if key in WeatherService.SUGGESTIONS:
            return WeatherService.SUGGESTIONS[key]

        # Generic fallback suggestions
        return [
            {'name': f'{city} City Center', 'desc': 'Explore the main downtown area and local cafes.', 'category': 'neighborhood'},
            {'name': f'{city} National Museum', 'desc': 'Local museum with cultural exhibits.', 'category': 'museum'},
            {'name': f'{city} Central Park', 'desc': 'Popular park for relaxing and walking.', 'category': 'park'},
            {'name': f'{city} Historic District', 'desc': 'Old town area with historic streets and buildings.', 'category': 'historic'},
        ]
    
    @staticmethod
    def parse_weather(data):
        """Parse weather data into readable format"""
        if not data or "error" in data:
            return None
        
        try:
            # Check if required fields exist
            if 'current_condition' not in data or not data['current_condition']:
                return {"error": "No weather data available"}
            
            current = data['current_condition'][0]
            
            # Check nearest_area exists
            if 'nearest_area' not in data or not data['nearest_area']:
                return {"error": "Location not found"}
            
            area = data['nearest_area'][0]
            
            return {
                'city': area.get('areaName', [{}])[0].get('value', 'Unknown'),
                'country': area.get('country', [{}])[0].get('value', 'Unknown'),
                'temperature': current.get('temp_C', 'N/A'),
                'temperature_f': current.get('temp_F', 'N/A'),
                'feels_like': current.get('FeelsLikeC', 'N/A'),
                'condition': current.get('weatherDesc', [{}])[0].get('value', 'Unknown'),
                'wind_speed': current.get('windspeedKmph', 'N/A'),
                'humidity': current.get('humidity', 'N/A'),
                'visibility': current.get('visibility', 'N/A'),
                'pressure': current.get('pressure', 'N/A'),
                'cloudcover': current.get('cloudcover', 'N/A'),
                'precipitation': current.get('precipMM', 'N/A'),
                'uv_index': current.get('uvIndex', 'N/A'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'suggestions': WeatherService.get_suggestions(area.get('areaName', [{}])[0].get('value', ''))
            }
        except (KeyError, IndexError, TypeError) as e:
            print(f"Parse error: {e}")
            print(f"Data structure: {data}")
            return None


@app.route('/')
def index():
    """Main page"""
    return render_template('weather.html')


@app.route('/api/weather', methods=['POST'])
def get_weather_api():
    """API endpoint to get weather"""
    try:
        city = request.json.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'City name required'}), 400
        
        weather_data = WeatherService.get_weather(city)
        
        # Check if there's an error in weather_data
        if weather_data and "error" in weather_data:
            return jsonify(weather_data), 400
        
        parsed = WeatherService.parse_weather(weather_data)
        
        if parsed and isinstance(parsed, dict) and "error" not in parsed:
            return jsonify(parsed)
        else:
            return jsonify({'error': 'Could not fetch weather data. Try another city or check spelling.'}), 400
    except Exception as e:
        print(f"API Error: {e}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/api/weather/<city>')
def get_weather_get(city):
    """GET endpoint to get weather"""
    weather_data = WeatherService.get_weather(city)
    parsed = WeatherService.parse_weather(weather_data)
    
    if parsed:
        return jsonify(parsed)
    else:
        return jsonify({'error': 'City not found'}), 404


if __name__ == '__main__':
    print("🌤️  Starting Weather App Server...")
    print("📍 Visit: http://localhost:5000")
    app.run(debug=True, port=5000)
