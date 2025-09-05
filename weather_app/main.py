from geo_api import GeoAPI
from weather_api import WeatherAPI
from weather_app import WeatherApp

API_KEY = "32754a42fb0647dc44d5b29a10aaa115"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"
BASE_GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"


def create_geo_api():
    geography_api = GeoAPI(BASE_GEO_URL, API_KEY, "Sydney")
    return geography_api


def get_geo_data(geography_api):
    geography_api.call_data()
    latitude, longitude, name = geography_api.get_location()
    return latitude, longitude, name


def create_weather_api(latitude, longitude):
    forecast_api = WeatherAPI(BASE_WEATHER_URL, API_KEY, latitude, longitude)
    return forecast_api


def get_weather_data(forecast_api):
    forecast_api.call_data()
    current_temp = forecast_api.get_current_temperature()
    return current_temp


def create_gui():
    weather_gui = WeatherApp()
    return weather_gui


def main():
    geography_api = create_geo_api()
    latitude, longitude, name = get_geo_data(geography_api)
    forecast_api = create_weather_api(latitude, longitude)
    current_temp = get_weather_data(forecast_api)
    weather_gui = create_gui()


if __name__ == '__main__':
    main()
