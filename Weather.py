import requests
from ss import weathKey

api_address = "http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=" + weathKey

try:
    json_data = requests.get(api_address).json()

    def temp():
        temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Convert temperature from Kelvin to Celsius
        return temperature

    def des():
        description = json_data["weather"][0]["description"]
        return description

    print("Temperature in Delhi:", temp(), "°C")
    print("Weather description in Delhi:", des())

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
