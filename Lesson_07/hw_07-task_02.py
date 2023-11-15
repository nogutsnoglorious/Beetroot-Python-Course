# Lesson 7 Homework; Task 2
# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
# The code has to return the dictionary with the sums of the prices by the goods types.

# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price_dict = {}

for el in prices.keys():
    item_total_price = 0
    for x in stock.keys():
        if el == x:
            item_total_price = prices.get(el) * stock.get(x)
        else:
            continue
    total_price_dict.update({el: item_total_price})

print("Final dictionary looks like this:", total_price_dict)

total_price = 0
for y in total_price_dict.values():
    total_price += y
print("Final price of all items is: ", total_price)
