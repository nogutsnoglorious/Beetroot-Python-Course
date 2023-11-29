# Lesson 11 Homework; Task 2
# Extend Phonebook application
# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program

# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application,
# else raise an error. After the user exits, all data should be saved to loaded JSON.

import json

file_path = "Lesson_11/phonebook.json"
default_entry = {
    "First Name": "",
    "Last Name": "",
    "Phone": "",
    "City": "",
    "State": "",
}

def read_file():
    try:
        with open(file_path, "r") as file_wrapper:
            data = json.load(file_wrapper)
            print(data)
    except FileNotFoundError:
        print("Error: No file with such name was found, but now it's created.")
        create_file()

def create_file():
    with open(file_path, "a") as file_wrapper:
        data = []
        json.dump(data, file_wrapper, indent=4)

def new_entry():
    with open(file_path, "r") as file:
        data = json.load(file)

    empty_data = {}
    for key in default_entry:
        new_value = input(f'Enter {key} of a new user: ')
        empty_data.update({key: new_value})
    data.append(empty_data)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def search_info():
    with open(file_path, "r") as file:
        data = json.load(file)
        search_request = input("Enter by what info should we search: ").title()
        found_info = False
        found_value = False
        if search_request in default_entry or search_request == 'Full Name':
            found_info = True

        if not found_info:
            print("There's no such parameter.")

        else:
            search_for = input(f'Enter users {search_request}: ').title()
            if search_request == 'Full Name':
                    for el in data:
                        full_name = el.get("First Name") + " " + el.get("Last Name") 
                        if full_name == search_for:
                            found_value = True
                            print("\n")
                            for key, value in el.items():
                                    print(f'{key}: {value}')    
            elif search_request != 'Full Name':
                for el in data: 
                    if el.get(search_request) != search_for:
                        continue
                    elif el.get(search_request) == search_for:
                        found_value = True
                        print("\n")
                        for key, value in el.items():
                            print(f'{key}: {value}')
                        break
            if not found_value:
                print(f'There is no such value for {search_request} in phonebook.')
                
def edit_record():
    with open(file_path, "r") as file:
        data = json.load(file)
        # print(data)
        user_found = False
        what_number = input("Enter a phone number are you interested in with XXX-XX-XX format: ")
        for index, el in enumerate(data):
            if el.get("Phone") == what_number:
                user_found = True
                dict_to_edit = el.copy()
                print(dict_to_edit)
                what_action = input("What do you want this user's record (edit/delete): ").lower()

                if what_action == "edit":
                    what_edit = input("What do you want to edit: ").title()
                    new_value = input(f'Enter new value for users {what_edit}: ')
                    dict_to_edit[what_edit] = new_value
                    data[index] = dict_to_edit

                elif what_action == "delete":
                    data.pop(index)

                with open(file_path, "w") as outfile:
                    json.dump(data, outfile, indent=4)
                
                break    

        if not user_found:
            print("There is no user with such phone number.")

def phonebook(action):
    if action == 'Show Phonebook':
        read_file()
    elif action == 'New Entry':
        new_entry()
    elif action == 'Search':
        search_info()
    elif action == 'Edit Record':
        edit_record()
    elif action == 'Exit':
        return True
    else:
        print("Unknown operation. Please, try again!")

action_list = ['Show Phonebook', 'New Entry', 'Search', 'Edit Record', 'Exit']

while True:
    print("\nHey! Here's a list of available options:\n")
    for el in action_list:
        print("-", el)
    action = input("\nWhat do you want to do: ").title()
    exit = phonebook(action)
    if exit == True:
        break