import asyncio
import aiohttp
import json

async def fetch_personnel_losses(date, session, results_dict):
    url = f"https://russianwarship.rip/api/v2/statistics/{date}"
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            personnel_losses = data['data']['stats']['personnel_units']
            results_dict[date] = personnel_losses
        else:
            print(f"Error fetching data for {date}. Status code: {response.status}")
            results_dict[date] = None

def calculate_increment(losses):
    increment = []
    for i in range(len(losses) - 3):
        inc = losses[i + 3] - losses[i]
        increment.append(inc)
    return increment

async def main():
    dates = ["2022-03-26", "2022-08-24", "2023-12-13", "2022-03-27", "2022-08-25", "2023-12-14"]
    results_dict = {}

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_personnel_losses(date, session, results_dict) for date in dates]
        await asyncio.gather(*tasks)

    losses = [results_dict[date] for date in dates if date in results_dict]

    increment = calculate_increment(losses)

    sorted_increment = sorted(enumerate(increment), key=lambda x: x[1], reverse=True)

    output_dict = {}
    for idx, inc in sorted_increment:
        i = idx % 3
        output_dict[dates[i]] = inc

    output_file = "Lesson_29/hw-29-task_2_result_asyncio.json"
    with open(output_file, 'w') as json_file:
        json.dump(output_dict, json_file)

    print("Results saved to:", output_file)

if __name__ == "__main__":
    asyncio.run(main())
