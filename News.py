import requests

# Assuming 'key' is defined somewhere in your 'ss' module
from ss import key

api_address = "http://newsapi.org/v2/top-headlines?country=us&apikey=" + key

json_data = requests.get(api_address).json()

def news():
    articles = json_data["articles"]
    headlines = []
    for i in range(3):
        headline = "Number " + str(i+1) + ": " + articles[i]["title"]
        headlines.append(headline)
    return headlines


