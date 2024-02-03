import requests

url = "http://www.wikipedia.org"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

    # Access specific fields in the JSON data
    title = data.get('title')
    body = data.get('body')[:10]

    print("Title:", title)
    print("Body:", body)
else:
    print(f"Request failed with status code {response.status_code}")
