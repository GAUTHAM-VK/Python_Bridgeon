import requests

url: str = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke: dict = response.json()

    print("😂 Random Joke")
    print()
    print("Setup:")
    print(joke["setup"])

    print()
    print("Punchline:")
    print(joke["punchline"])
else:
    print("Could not get joke.")