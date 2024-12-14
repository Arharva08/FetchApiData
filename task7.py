import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Output:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
