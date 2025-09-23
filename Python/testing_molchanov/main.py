import requests


def add(a, b):
    return a + b

def get_joke():
    link = "https://api.chucknorris.io/jokes/random"

    response = requests.get(link)
    return response.json()["value"]


def len_joke():
    joke = get_joke()
    return len(joke)