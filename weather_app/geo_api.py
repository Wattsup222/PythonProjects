import requests


class GeoAPI:
    def __init__(self, base_url, api_key, city):
        self.base_url = base_url
        self.api_key = api_key
        self.city = city
        self.endpoint_url = f"{self.base_url}?q={self.city}&limit=1&appid={self.api_key}"
        self.geo_data = None

    def access_data(self):
        response = requests.get(self.endpoint_url)
        print(response)  # test

        if response.status_code == 200:
            self.geo_data = response.json()
            print(self.geo_data)  # test
        else:
            print(f"Failed to get data from API {response.status_code}")

    def get_location(self):
        pass
