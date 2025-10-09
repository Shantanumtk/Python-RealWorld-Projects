import requests

def get_news_headlines():
    api_key = "API_KEY"
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country=us&max=5&apikey={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching news: ", response.status_code)
        return
    
    data = response.json()

    print(data["information"]["realTimeArticles"]["message"])
    
    print("Top 5 News Headlines:\n")
    for article in data["articles"]:
        print("Title: ", article["title"])
        print("URL:", article["url"])

if __name__ == "__main__":
    get_news_headlines()