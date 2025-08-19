import requests

base_url = "https://api.openweathermap.org/data/2.5/weather?q=Sydney&units=metric&appid=32754a42fb0647dc44d5b29a10aaa115"


def call_weather_data():
    response = requests.get(base_url)
    print(response)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return weather_data
    else:
        print(f"Failed to retrieve weather data {response.status_code}")


def get_weather_info(weather_data):
    if weather_data:
        print(f"{weather_data["weather"][0]["main"]}")


def main():
    weather_data = call_weather_data()
    get_weather_info(weather_data)


if __name__ == '__main__':
    main()
