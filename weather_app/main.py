import requests

API_KEY = "32754a42fb0647dc44d5b29a10aaa115"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"
BASE_GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"


def update_geo_url(city):
    modified_geo_url = f"{BASE_GEO_URL}?q={city}&limit=1&appid={API_KEY}"
    return modified_geo_url


def call_geo_data(modified_geo_url):
    response = requests.get(modified_geo_url)
    print(response)

    if response.status_code == 200:
        geo_data = response.json()
        print(geo_data)
        return geo_data
    else:
        print(f"Failed to retrieve geo data {response.status_code}")
        return None


def location(geo_data):
    name = geo_data[0]["name"]
    latitude = geo_data[0]["lat"]
    longitude = geo_data[0]["lon"]
    print(name, latitude, longitude)
    return latitude, longitude, name


def update_weather_url(latitude, longitude):
    modified_weather_url = f"{BASE_WEATHER_URL}?lat={latitude}&lon={longitude}&units=metric&appid={API_KEY}"
    return modified_weather_url


def call_weather_data(modified_weather_url):
    response = requests.get(modified_weather_url)
    print(response)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return weather_data
    else:
        print(f"Failed to retrieve weather data {response.status_code}")
        return None


def get_weather_info(weather_data):
    if weather_data:
        print(f"{weather_data["current"]}")


def main():
    modified_geo_url = update_geo_url("Sydney")
    geo_data = call_geo_data(modified_geo_url)
    latitude, longitude, name = location(geo_data)
    modified_weather_url = update_weather_url(latitude, longitude)
    weather_data = call_weather_data(modified_weather_url)
    get_weather_info(weather_data)


if __name__ == '__main__':
    main()
