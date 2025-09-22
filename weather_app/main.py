import tkinter as tk
from tkinter import ttk
from geo_api import GeoAPI
from weather_api import WeatherAPI

API_KEY = "32754a42fb0647dc44d5b29a10aaa115"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"
BASE_GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"


def gui_setup():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("600x700")
    return root


def get_city(root):
    city_var = tk.StringVar()

    city_label = ttk.Label(root, text="City:")
    city_label.pack()

    city_entry = ttk.Entry(root, textvariable=city_var)
    city_entry.pack()

    search_button = ttk.Button(
        root,
        text="Search",
        command=lambda: submit(city_var, root)
    )
    search_button.pack()


def submit(city_var, root):
    city = city_var.get()
    print("City entered:", city)

    geography_api = create_geo_api(city)
    latitude, longitude, name = get_geo_data(geography_api)

    forecast_api = create_weather_api(latitude, longitude)
    current_temp = get_weather_data(forecast_api)

    result_label = ttk.Label(root, text=f"{name}: {current_temp}°C")
    result_label.pack()


def create_geo_api(city):
    return GeoAPI(BASE_GEO_URL, API_KEY, city)


def get_geo_data(geography_api):
    geography_api.call_data()
    latitude, longitude, name = geography_api.get_location()
    return latitude, longitude, name


def create_weather_api(latitude, longitude):
    return WeatherAPI(BASE_WEATHER_URL, API_KEY, latitude, longitude)


def get_weather_data(forecast_api):
    forecast_api.call_data()
    return forecast_api.get_current_temperature()


def main():
    root = gui_setup()
    get_city(root)
    root.mainloop()


if __name__ == '__main__':
    main()
