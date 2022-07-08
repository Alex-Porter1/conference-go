from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import json
import requests


def get_photo(city, state):
    headers = {"Authorization": PEXELS_API_KEY}
    url = "https://api.pexels.com/v1/search"
    params = {
        "per_page": 1,
        "query": city + " " + state
    }
    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)
    try:
        return{"picture_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": None}


def get_weather(city, state):
    params = {
        "q": f"{city}, {state}, US",
        "limit": 1,
        "appid": OPEN_WEATHER_API_KEY
    }
    url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(url, params=params)
    content = json.loads(response.content)

    try:
        latitude = content[0]["lat"]
        longitude = content[0]["lon"]
    except(KeyError, IndexError):
        return None

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial"
    }

    url = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=params)
    content = json.loads(response.content)

    try:
        return {
            "description": content["weather"][0]["description"],
            "temp": content["main"]["temp"],
        }
    except(KeyError, IndexError):
        return None
