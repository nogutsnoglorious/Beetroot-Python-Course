# Lesson 13 Classwork; Task 5
# Напишіть функцію apply_discount, яка приймає суму покупки та іншу функцію discount_func для обчислення знижки.
# Функція повинна виводити суму знижки та загальну суму після застосування знижки.

purchase_list = []   # list of prices for purchased items
while True:
    item_price = input("Enter item's price you buy: ")
    if item_price == "":
        break
    else:
        purchase_list.append(int(item_price))

purchase_sum = (lambda x: sum(x))(purchase_list)    # function that calculates total sum of purchased items

def discount_func(x):
    if x < 1000:
        return .1
    elif 1000 <= x < 5000:
        return .2
    else:
        return .5
    
def apply_discount(x, func):
    discount_value = x*func(x)
    sum_after_discount = x - discount_value
    print(f'Thanks!\nYour total sum before discount is {purchase_sum}.\nYour discount value is {round(discount_value,1)}.\nYour final price after discount is {sum_after_discount}.')

apply_discount(x = purchase_sum, func = discount_func)