import requests
import json
import pyttsx3

city = input("Enter the city where you want to check weather : ")

url =f"https://api.weatherapi.com/v1/current.json?key=d93e6209e8fb4a249e4102339232306&q={city}"

engine = pyttsx3.init()
r=requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
engine.say(f"The temperature in {city} is {w}")
engine.runAndWait()
