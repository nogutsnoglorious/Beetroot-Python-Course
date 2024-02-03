# identify losses for certain days and print it in descending order

import requests

def fetch_personnel_losses(dates):
    losses = []
    for date in dates:
        url = f"https://russianwarship.rip/api/v2/statistics/{date}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            personnel_losses = data['data']['stats']['personnel_units']
            losses.append(personnel_losses)
        else:
            print(f"Error. Status code: {response.status_code}")
    return losses

def calculate_increment(losses):
    increment = []
    for i in range(len(losses) - 3):
        inc = losses[i + 3] - losses[i]
        increment.append(inc)
    return increment

dates = ["2022-03-26", "2022-08-24", "2023-12-13", "2022-03-27", "2022-08-25", "2023-12-14"]
losses = fetch_personnel_losses(dates)
increment = calculate_increment(losses)

# Sort in descending order
sorted_increment = sorted(enumerate(increment), key=lambda x: x[1], reverse=True)

for idx, inc in sorted_increment:
    i = idx % 3
    print(f"Personnel loss increment for {dates[i]} was {inc}.")
