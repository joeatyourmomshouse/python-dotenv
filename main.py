import os
from dotenv import load_dotenv
import requests

load_dotenv()
key = os.getenv("key")

city = "Torronto"

url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=imperial")

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    print(f"The current temperature in {city} is {temp}°F.")

else:
    print(f"Error fetching weather data: {data['message']}")


