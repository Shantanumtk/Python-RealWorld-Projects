# 01-Weather API

Tiny Python script that prints the **current weather** for a city using **Open‑Meteo** (free, no API key).

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate   # macOS/Linux
# Windows: .venv\Scripts\activate
pip install requests
```

## File

Save as `weather_now.py`:

```python
import sys, requests
city=sys.argv[1] if len(sys.argv)>1 else "San Francisco"; country=sys.argv[2] if len(sys.argv)>2 else None
gp={"name":city,"count":1,"language":"en","format":"json"}; gp.update({"country":country} if country else {})
g=requests.get("https://geocoding-api.open-meteo.com/v1/search",params=gp,timeout=15).json()
if not g.get("results"): raise SystemExit(f"No matches for '{city}'. Try COUNTRY code (US, IN, ...).")
p=g["results"][0]
f=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":p["latitude"],"longitude":p["longitude"],"timezone":p.get("timezone"),"current_weather":True},timeout=20).json()
cw=f.get("current_weather",{})
print(f'{p.get("name")}, {p.get("country")} | TZ {f.get("timezone")} | {cw.get("temperature")}°C, wind {cw.get("windspeed")} km/h, code {cw.get("weathercode")}')
```

## Run

```bash
python weather_now.py                 # defaults to San Francisco
python weather_now.py "Mumbai"        # custom city
python weather_now.py Paris FR        # city + country code
```

## Optional tweaks

* **Fahrenheit / mph**: add to the forecast params:

  ```python
  "temperature_unit":"fahrenheit","windspeed_unit":"mph"
  ```
* Change the default city by editing the first line.

## Notes

* Uses Open‑Meteo (no key, free).
* If you see “No matches…”, pass a country code (e.g., `US`, `IN`, `GB`).
