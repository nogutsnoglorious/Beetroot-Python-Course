from datetime import datetime

name = "Valentyn"
today = datetime.now().strftime('%A')
day = "Tuesday"

print(f'Good day {name}! {today} is a perfect day to learn some Python.')

# second option

print("Good day %s! %s is a perfect day to learn some Python." % (name, day))