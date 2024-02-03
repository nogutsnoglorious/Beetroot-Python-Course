# identify resource for certain day and open it in browser tab

import requests
import webbrowser

stats_url = "https://russianwarship.rip/api/v2/statistics/2024-02-02"
stats_response = requests.get(stats_url)
data = stats_response.json()

if 'data' in data and 'resource' in data['data']:
    resource_url = data['data']['resource']
    print("Resource URL:", resource_url)

    webbrowser.open(resource_url)
else:
    print("Resource field not found in the response.")