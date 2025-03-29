import requests
import json
import sys

## make a tool to decide what to do with my kid, based on the weather today



def get_weather_data(city: str) -> dict:
    """Fetch weather data from OpenWeatherMap API for a given city."""
    api_key = "YOURAPI"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200: 
        weather_dic = {}
        data = response.json()
        weather_dic["country"] = data["sys"]["country"]
        weather_dic["city"] = data["name"]
        weather_dic["weather"] = data["weather"][0]["main"]
        weather_dic["temperature"] = data["main"]["temp"]
        return weather_dic
    else:
        sys.exit(
            f"Failed to fetch data. Check key or city. Response: {response.text}"
        )


def weather_icon(weather: str):
    weather_icons_dic = {
        "Clear": "☀️",  # Sun
        "Clouds": "☁️",  # Cloud
        "Rain": "🌧️",  # Rain cloud
        "Drizzle": "🌦️",  # Sun with rain
        "Snow": "❄️",  # Snowflake
        "Thunderstorm": "⛈️",  # Thunderstorm
        "Mist": "🌫️",  # Fog/mist
        "Fog": "🌫️",  # Fog/mist
        "Haze": "🌫️",  # Similar to mist
        "Smoke": "💨",  # Wind/smoke
        "Dust": "💨",  # Wind/dust
        "Sand": "💨",  # Wind/sand
        "Ash": "💨",  # Wind/ash
        "Squall": "🌬️",  # Wind
        "Tornado": "🌪️",  # Tornado
    }
    return weather_icons_dic.get(weather, "🌐")


def decide_activity(weather: str) -> str:
    """Decide what to do based on the weather data today"""
    task = {
        "Clear": "Go for a walk in the nature",
        "Clouds": "Go for a walk in the nature",
        "Rain": "Stay indoors or go shopping",
        "Snow": "Play with the snow or go skiing",
        "Thunderstorm": "Stay indoors and read a book together",
        "Drizzle": "Stay indoors and read a book together",
        "Mist": "Perhaps take a walk",
        "Fog": "Stay indoors",
        "Haze": "Stay indoors",
        "Smoke": "Stay indoors, it is smokey outside",
        "Dust": "Stay indoors, it is dusty outside",
        "Sand": "Stay indoors, too much sand outside",
        "Ash": "Stay safe indoors, it is ashy outside",
        "Squall": "Stay indoors",
        "Tornado": "Maybe we shall move to another city and stay there for a while",
    }
    return task.get(weather, "No specific task assigned for this weather")


def decide_clothing(temp: float) -> str:
    """Decide what to wear based on the temperature"""
    if temp > 25:
        return "Wear shorts and a t-shirt"
    elif 15 < temp <= 25:
        return "Wear a light jacket and think pants"
    elif 5 < temp <= 15:
        return "Wear a warm jacket and thick pants"
    else:
        return "Wear a heavy coat"



def main(): 
    city = input("Enter the city name: ")
    weather_data = get_weather_data(city)
    if weather_data:
        country = weather_data["country"]
        city = weather_data["city"]
        weather = weather_data["weather"]
        temperature = weather_data["temperature"]
        icon = weather_icon(weather)
        suggestion = decide_activity(weather)
        clothing = decide_clothing(temperature)
        print(f"\n\nToday in {city}, {country}: {icon} {weather}, {temperature}°C. "
              f"\n\nSuggested activity: {suggestion}\nSuggested clothing: {clothing}", end="\n\n")
    else:
        print("Could not retrieve weather data.")


if __name__ == "__main__":
    main()
