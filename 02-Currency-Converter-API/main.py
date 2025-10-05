# currency_converter.py
import requests

base = input("From (e.g., USD): ").upper().strip()
to   = input("To   (e.g., INR): ").upper().strip()
amt  = float(input("Amount: ").strip() or 1)

url = f"https://api.frankfurter.app/latest?amount={amt}&from={base}&to={to}"
try:
    rate = requests.get(url, timeout=10).json().pretty()
    print(rate)
    rate2 = requests.get(url, timeout=10).json()["rates"][to]
    print(f"{amt:.2f} {base} = {rate2:.4f} {to}")
    date = requests.get(url,timeout=10).json()["date"]
    print (date)
except Exception as e:
    print("Conversion failed. Check currency codes / internet.")
