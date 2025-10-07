import requests

def get_joke():
    URL = "https://official-joke-api.appspot.com/random_joke"
    try:
        r = requests.get(URL,timeout=10)
        r.raise_for_status()
        data = r.json()
        print(data['setup'])
        print(data['punchline'])
    except Exception as e:
        print("Error fetching Joke:", e)

if __name__ == "__main__":
    get_joke()