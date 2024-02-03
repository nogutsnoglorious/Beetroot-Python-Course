# 1. Отримайте поточний статус війни як англійською, так і українською мовою.
# 2. Отримайте останню статистику по війні
# 3. Отримайте статистику за 2 різні дні (виберіть дату самостійно).

import requests

status_en_url = "https://russianwarship.rip/api/v2/war-info/status/en"
status_en_response = requests.get(status_en_url)
print(status_en_response.json())

status_ua_url = "https://russianwarship.rip/api/v2/war-info/status/ua"
status_ua_response = requests.get(status_ua_url)
print(status_ua_response.json())

stats_url = "https://russianwarship.rip/api/v2/statistics/latest"
stats_response = requests.get(stats_url)
print(stats_response.json())

stats_day1_url = "https://russianwarship.rip/api/v2/statistics/2023-01-01"
stats_day1_response = requests.get(stats_day1_url)
print(stats_day1_response.json())

stats_day2_url = "https://russianwarship.rip/api/v2/statistics/2024-01-01"
stats_day2_response = requests.get(stats_day2_url)
print(stats_day2_response.json())


