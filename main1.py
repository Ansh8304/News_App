import requests

api = "8b3c5c45f5de47bebe6420a6219e0f0f"

query = input("Enter Which type of news you want to explore")

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-11&sortBy=publishedAt&apiKey={api}"

news  = requests.get(url).json()

articles = news["articles"]

print(url)
for article in articles:
    print(article["title"])
    print(article["url"])

    print("\n\n")