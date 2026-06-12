import requests

url: str = "https://api.github.com/users/octocat"

response = requests.get(url)

if response.status_code == 200:
    data: dict = response.json()

    print("GitHub User Details")
    print("-------------------")
    print(f"Name         : {data['name']}")
    print(f"Location     : {data['location']}")
    print(f"Public Repos : {data['public_repos']}")
    print(f"Created At   : {data['created_at']}")
else:
    print("Failed to fetch data")