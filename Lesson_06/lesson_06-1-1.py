name = input("Enter client's name: ")
order = list()
dishlist = list()
dishqty = 0
exit == False
while exit == False:
    dish = input("Enter desired dish(es): ")
    if dish.isalpha() and dish != "":
        dishlist.append(dish)
    elif dish.isalnum or dish == "":
        print("Done!")
        dishqty = len(dishlist)
        exit == True
order.append(name)
order.extend(dishlist)
order.append(dishqty)
print(order)
