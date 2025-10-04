# weather_now.py
import sys, requests
city=sys.argv[1] if len(sys.argv)>1 else "San Francisco"; 
country=sys.argv[2] if len(sys.argv)>2 else None
gp={"name":city,"count":1,"language":"en","format":"json"}; 
gp.update({"country":country} if country else {})

g=requests.get("https://geocoding-api.open-meteo.com/v1/search",params=gp,timeout=15).json()

if not g.get("results"): raise SystemExit(f"No matches for '{city}'. Try COUNTRY code (US, IN, ...).")

p=g["results"][0]

f=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":p["latitude"],"longitude":p["longitude"],"timezone":p.get("timezone"),"current_weather":True},timeout=20).json()
cw=f.get("current_weather",{})
print(f'{p.get("name")}, {p.get("country")} | TZ {f.get("timezone")} | {cw.get("temperature")}°C, wind {cw.get("windspeed")} km/h, code {cw.get("weathercode")}')
