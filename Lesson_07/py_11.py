order_list = [("Order 4534637", 1334), ("Order 435346", 122223), ("Order 53334", 664), ("Order 22214", 6673)]
total_sum = 0
for el in order_list:
    total_sum = total_sum + list(el)[1]
print("Total sum for all orders is", total_sum)