phonebook = {
    "John": "4353463",
    "Barry": "435437",
    "Walt": "3356235"
}

while True:
    question_1 = input("Do you want to add new contact? ")
    if question_1 != "":
        add_name = input("Add new contact name: ")
        add_phone = input(f'Add {add_name}s phone number: ')
        phonebook.update({add_name: add_phone})
        continue
    else:
        question_2 = input("Do you want to search existing contact? ")
        if question_2 != "":
            search_name = input("Enter contacts name: ")
            print(f'Here is contacts contact number phonebook {phonebook.get(search_name)}')
            break
        else:
            break

print("Thanks, bye!")
