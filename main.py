import requests

def get_weather (city, units="metric", api_key="42c9901c8030442cc56a1cd0a8e582b1"):
  url= f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r=requests.get(url)
  content= r.json()
  with open("data.txt", "a") as file:
    for dicty in content["list"]:
      file.write(f"{city}, {dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
print(get_weather(city="Constanta"))

