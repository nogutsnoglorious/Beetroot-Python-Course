# Lesson 8 Homework; Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name
# and capital as parameters. Then create a dictionary from those two,
# with ‘name’ as a key and ‘capital’ as a parameter. Make the function
# print out the values of the dictionary to make sure that it works as intended.

countries_dict = dict()

def create_dict(x,y):
    countries_dict.update({x: y})

while True:
    country = input("Enter country: ")
    capital = input("Enter capital: ")
    if country == "" or capital == "":
        break
    else:
        create_dict(country,capital)

print('Your country list is: {}.'.format(countries_dict))