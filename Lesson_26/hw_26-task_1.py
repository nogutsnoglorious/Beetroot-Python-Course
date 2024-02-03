# get robots.txt from certain resources

import requests

# Wikipedia
url_1 = 'https://en.wikipedia.org/robots.txt'

try:
    response = requests.get(url_1)
    if response.status_code == 200:
        file_path = 'Lesson_26/wiki_robots.txt'

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Robots.txt file saved as {file_path}")
    else:
        print(f"Error. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Google
url_2 = 'https://google.com/robots.txt'

try:
    response = requests.get(url_2)
    if response.status_code == 200:
        file_path = 'Lesson_26/google_robots.txt'

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Robots.txt file saved as {file_path}")
    else:
        print(f"Error. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Spotify
url_3 = 'https://spotify.com/robots.txt'

try:
    response = requests.get(url_3)
    if response.status_code == 200:
        file_path = 'Lesson_26/spotify_robots.txt'

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Robots.txt file saved as {file_path}")
    else:
        print(f"Error. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")