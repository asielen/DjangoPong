import requests
import json

API = '44d1d115968f5b7e6b56551cd1778252'
API_NEW = 'e4c5c679f2df4a48fad14a2833cd6e2e'
LOCID = 5391959
def _k_to_f(kelvin):
    return kelvin * (9 / 5) - 459.67

def get_weather():
    weather = {"temp":"??","icon":"https://openweathermap.org/img/w/02d.png"}
    try:
        j = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}".format(LOCID,API))
        weather_j = json.loads(j.content)
        weather["icon"] = "https://openweathermap.org/img/w/{}.png".format(weather_j["weather"][0]["icon"])
        weather["temp"] = str(int(round(_k_to_f(weather_j["main"]["temp"]),0)))
    except Exception as e:
        print("Can't get weather Icon",e)
    return weather

get_weather()
