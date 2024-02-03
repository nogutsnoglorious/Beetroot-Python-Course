import requests
import json
import threading

def fetch_personnel_losses(date, results_dict):
    url = f"https://russianwarship.rip/api/v2/statistics/{date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        personnel_losses = data['data']['stats']['personnel_units']
        results_dict[date] = personnel_losses
    else:
        print(f"Error fetching data for {date}. Status code: {response.status_code}")
        results_dict[date] = None

def calculate_increment(losses):
    increment = []
    for i in range(len(losses) - 3):
        inc = losses[i + 3] - losses[i]
        increment.append(inc)
    return increment

def main():
    dates = ["2022-03-26", "2022-08-24", "2023-12-13", "2022-03-27", "2022-08-25", "2023-12-14"]
    results_dict = {}

    threads = []
    for date in dates:
        thread = threading.Thread(target=fetch_personnel_losses, args=(date, results_dict))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Extracting losses from results_dict
    losses = [results_dict[date] for date in dates if date in results_dict]

    increment = calculate_increment(losses)

    sorted_increment = sorted(enumerate(increment), key=lambda x: x[1], reverse=True)

    output_dict = {}
    for idx, inc in sorted_increment:
        i = idx % 3
        output_dict[dates[i]] = inc

    output_file = "Lesson_28/hw-28-task_3_result_threading.json"
    with open(output_file, 'w') as json_file:
        json.dump(output_dict, json_file)

    print("Results saved to:", output_file)

if __name__ == "__main__":
    main()
