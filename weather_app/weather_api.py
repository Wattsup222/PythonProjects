class WeatherAPI:
    def __init__(self, base_url, key, latitude, longitude):
        self.base_url = base_url
        self.key = key
        self.latitude = latitude
        self.longitude = longitude
