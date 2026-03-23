import requests
import sys

def get_weather(city_name):

  geo_location_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    
  try:
    geo_res = requests.get(geo_location_url).json()
    if not geo_res.get('results'):
      print(f"Error: Could not find city '{city_name}'")
      return
        
    location = geo_res['results'][0]
    lat, lon = location['latitude'], location['longitude']

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=True"
    weather_data = requests.get(weather_url).json()
        
    current = weather_data['current_weather']
    temp_c = current['temperature']
    temp_f = (temp_c * 9/5) + 32

    print(f"\n--- Weather in {location['name']}, {location['country']} ---")
    print(f"Temperature: {temp_c}°C ({temp_f:.1f}°F)")
    print(f"Wind Speed: {current['windspeed']} km/h")
    print(f"Weather Code: {current['weathercode']} (Refer to docs for description)")

  except Exception as e:
    print(f"Error fetching weather: {e}")

if __name__ == "__main__":
  city = sys.argv[1] if len(sys.argv) > 1 else "Lahore"
  get_weather(city)