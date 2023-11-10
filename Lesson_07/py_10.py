student_list = [("John", 3.4), ("Jim", 4.5), ("Larry", 5.0), ("Hank", 2.2), ("Winston", 4.1)]
highest_mark = 0
name_index = ""
for i in student_list:
    if list(i)[1] > highest_mark:
            highest_mark = list(i)[1]
            name_index = list(i)[0]
print("Best stydent name is", name_index, "with average score of", highest_mark)
