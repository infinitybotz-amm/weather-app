"""
Simple Weather Fetcher - Minimal version
Quick script to fetch weather data
"""

import requests


def get_weather(city):
    """
    Fetch weather data from wttr.in API
    
    Args:
        city (str): City name
    
    Returns:
        dict: Weather data or None
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None


def display_weather(city):
    """Display weather information for a city"""
    data = get_weather(city)
    
    if not data:
        return
    
    try:
        current = data['current_condition'][0]
        
        print(f"\n🌍 Weather in {city}")
        print(f"Temperature: {current['temp_C']}°C ({current['temp_F']}°F)")
        print(f"Condition: {current['weatherDesc'][0]['value']}")
        print(f"Wind Speed: {current['windspeedKmph']} km/h")
        print(f"Humidity: {current['humidity']}%")
        print(f"Feels Like: {current['FeelsLikeC']}°C\n")
        
    except (KeyError, IndexError) as e:
        print(f"Error parsing data: {e}")


if __name__ == "__main__":
    # Example usage
    city = input("Enter city name: ").strip()
    if city:
        display_weather(city)
    else:
        print("Please enter a city name!")
