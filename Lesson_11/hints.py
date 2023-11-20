# TXT file
file_data = open("practice.txt", "r")
data = file_data.read()
print(data)
file_data.close()


# JSON file
with open("virtual_machines.json", "r") as file_wrapper:
    data = json.load(file_wrapper)
    print(data)


# CSV file
rows = []
with open("nestle_employee.csv", "r") as csv_wrapper:
    csv_reader = csv.reader(csv_wrapper)
    fields = next(csv_reader)
 
    for row in csv_reader:
        rows.append(row)

print(rows)