# implementation of hw_26-task_2 using multiprocessing approach

import requests
import json
import multiprocessing

def fetch_personnel_losses(date):
    url = f"https://russianwarship.rip/api/v2/statistics/{date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        personnel_losses = data['data']['stats']['personnel_units']
        return {date: personnel_losses}
    else:
        print(f"Error. Status code: {response.status_code}")
        return {date: None}

def calculate_increment(losses):
    increment = []
    for i in range(len(losses) - 3):
        inc = losses[i + 3] - losses[i]
        increment.append(inc)
    return increment

def main():
    dates = ["2022-03-26", "2022-08-24", "2023-12-13", "2022-03-27", "2022-08-25", "2023-12-14"]

    with multiprocessing.Pool(processes=len(dates)) as pool:
        results = pool.map(fetch_personnel_losses, dates)

    losses = [list(data.values())[0] for data in results]
    increment = calculate_increment(losses)

    sorted_increment = sorted(enumerate(increment), key=lambda x: x[1], reverse=True)

    results_dict = {}
    for idx, inc in sorted_increment:
        i = idx % 3
        results_dict[dates[i]] = inc

    output_file = "Lesson_27/hw-27-task_2_result_multiprocess.json"
    with open(output_file, 'w') as json_file:
        json.dump(results_dict, json_file)

    print("Results saved to:", output_file)

if __name__ == "__main__":
    main()
