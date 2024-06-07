import requests
import json

import pyttsx3
import os

city = input("Enter the name of the city\n")

# Use an f-string to correctly format the URL with the city name
url = f"https://api.weatherapi.com/v1/current.json?key=b1669ea07cf444988fe182830242005&q={city}"
r = requests.get(url)
json.loads(r.text)
wdic=json.loads(r.text)
# Print the response text
# print(r.text)
w=wdic["current"]["temp_c"]
engine = pyttsx3.init()
engine.say(f"'the current weather in {city} is {w} degrees")
engine.runAndWait()
# w=wdic["current"]["temp_c"]
os.system("current weather in given city: {city} is {w} degrees")
