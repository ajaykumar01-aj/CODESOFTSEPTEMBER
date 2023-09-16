import requests

def get_weather_data(api_key, location):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'appid': api_key, 'units': 'metric'}  # Use 'imperial' for Fahrenheit
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error fetching weather data.')
        return None

def display_weather_data(data):
    if data:
        main_data = data['main']
        weather_data = data['weather'][0]
        wind_data = data['wind']

        print(f'Location: {data["name"]}, {data["sys"]["country"]}')
        print(f'Temperature: {main_data["temp"]}°C')
        print(f'Humidity: {main_data["humidity"]}%')
        print(f'Weather: {weather_data["description"]}')
        print(f'Wind Speed: {wind_data["speed"]} m/s')

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    location = input('Enter city name or zip code: ')
    
    weather_data = get_weather_data(api_key, location)
    
    if weather_data:
        display_weather_data(weather_data)

if __name__ == '__main__':
    main()
