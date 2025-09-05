import requests


class WeatherAPI:
    def __init__(self, base_url, key, latitude, longitude):
        self.base_url = base_url
        self.key = key
        self.latitude = latitude
        self.longitude = longitude
        self.endpoint_url = f"{self.base_url}?lat={self.latitude}&lon={self.longitude}&units=metric&appid={self.key}"
        self.weather_data = None

    def call_data(self):
        response = requests.get(self.endpoint_url)
        print(response)  # test
        if response.status_code == 200:  # status OK
            self.weather_data = response.json()  # convert data to json format
            print(self.weather_data)  # test
        else:
            print(f"Failed to get data from API {response.status_code}")

    def get_current_temperature(self):
        current_temp = self.weather_data["current"]["temp"]
        return current_temp
