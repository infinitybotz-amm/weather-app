"""
Simple Weather Application using wttr.in API
Fetches current weather data for any city
"""

import requests
import json
from datetime import datetime


class WeatherApp:
    """
    Weather Application class to fetch weather data from wttr.in API
    """
    
    BASE_URL = "https://wttr.in"
    
    def __init__(self):
        self.session = requests.Session()
    
    def get_weather(self, city, format='j1'):
        """
        Fetch current weather data for a city
        
        Args:
            city (str): City name
            format (str): Response format ('j1' for JSON, 'text', etc.)
        
        Returns:
            dict: Weather data or None if request fails
        """
        try:
            # Build URL with format parameter
            url = f"{self.BASE_URL}/{city}?format={format}"
            
            print(f"🌍 Fetching weather for: {city}...")
            
            # Make API request
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            if format in ['j1', 'json']:
                return response.json()
            else:
                return response.text
                
        except requests.exceptions.ConnectionError:
            print("❌ Error: Could not connect to weather service")
            return None
        except requests.exceptions.Timeout:
            print("❌ Error: Request timed out")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"❌ Error: {e.response.status_code} - City not found")
            return None
        except json.JSONDecodeError:
            print("❌ Error: Could not parse weather data")
            return None
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def display_current_weather(self, city):
        """
        Fetch and display current weather for a city
        
        Args:
            city (str): City name
        """
        weather_data = self.get_weather(city, format='j1')
        
        if not weather_data:
            return
        
        try:
            # Extract current weather data
            current = weather_data.get('current_condition', [{}])[0]
            
            # Display formatted weather information
            print("\n" + "="*50)
            print(f"📍 Weather in {city.upper()}")
            print("="*50)
            print(f"🌡️  Temperature: {current.get('temp_C', 'N/A')}°C ({current.get('temp_F', 'N/A')}°F)")
            print(f"💨 Wind Speed: {current.get('windspeedKmph', 'N/A')} km/h")
            print(f"💧 Humidity: {current.get('humidity', 'N/A')}%")
            print(f"👁️  Visibility: {current.get('visibility', 'N/A')} km")
            print(f"🌫️  Pressure: {current.get('pressure', 'N/A')} mb")
            print(f"☁️  Cloud Cover: {current.get('cloudcover', 'N/A')}%")
            print(f"📝 Weather: {current.get('weatherDesc', [{}])[0].get('value', 'N/A')}")
            print(f"🌧️  Precipitation: {current.get('precipMM', 'N/A')} mm")
            print(f"💦 Feels Like: {current.get('FeelsLikeC', 'N/A')}°C")
            print("="*50 + "\n")
            
        except (KeyError, IndexError, TypeError) as e:
            print(f"❌ Error parsing weather data: {str(e)}")
    
    def get_weather_raw(self, city):
        """
        Get weather in plain text format
        
        Args:
            city (str): City name
        """
        return self.get_weather(city, format='text')
    
    def get_weather_json(self, city):
        """
        Get weather as JSON object
        
        Args:
            city (str): City name
        
        Returns:
            dict: Full JSON weather data
        """
        return self.get_weather(city, format='j1')


def main():
    """Main application"""
    print("\n" + "🌤️ "*10)
    print("WEATHER APPLICATION - Using wttr.in API")
    print("🌤️ "*10 + "\n")
    
    # Create weather app instance
    app = WeatherApp()
    
    while True:
        print("\nOptions:")
        print("1. Get current weather for a city")
        print("2. Get weather in plain text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            if city:
                app.display_current_weather(city)
            else:
                print("❌ Please enter a valid city name")
                
        elif choice == '2':
            city = input("Enter city name: ").strip()
            if city:
                print(f"\n📝 Weather for {city}:\n")
                weather = app.get_weather_raw(city)
                if weather:
                    print(weather)
            else:
                print("❌ Please enter a valid city name")
                
        elif choice == '3':
            print("\n👋 Thank you for using Weather App!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
