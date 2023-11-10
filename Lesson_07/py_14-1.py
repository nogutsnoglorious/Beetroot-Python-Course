total_orders = [
                ('John', ['cookies', 0.5, 3], ['biscuits', 1.5, 2], ['ice-cream', 0.9, 10]),
                ('Jim', ['glasses', 20, 1], ['smartwatches', 115, 2], ['bags', 0.2, 20], ['pop-corn', 1.2, 15]),
                ('Kylie', ['lipstick', 7.5, 30], ['bubblegum', 1.5, 2000])           
]

first_order = 0
first_list = total_orders[0]
for el in first_list:
    if type(el) == list:
        first_order = first_order + list(el)[1] * list(el)[2]

second_order = 0
second_list = total_orders[1]
for el in second_list:
    if type(el) == list:
        second_order = second_order + list(el)[1] * list(el)[2]

third_order = 0
third_list = total_orders[2]
for el in third_list:
    if type(el) == list:
        third_order = third_order + list(el)[1] * list(el)[2]

total_sum = [first_order, second_order, third_order]

print("There are", len(total_orders), "orders in total.")
print(f'First order is {int(total_sum[0])}.')
print(f'Second order is {int(total_sum[1])}.')
print(f'Third order is {int(total_sum[2])}.')

total_sum.sort()
print("The most expensive order is", int(total_sum[-1]))





    # for x in el:
    #     if type(x) == list: 
    #         print(x)
#    first_order = first_order + el[] 
# second_list = []
# third_list = []





# for el in total_orders:
#    print(el)
#        if el == 0:
#            for i in el:
#                if type(i) == list:
#                    print(i)
                    #for x in i:
                       # print(x)
                      #  first_order = first_order + list(x)[1] * list(x)[2]
           # if i != 0:
                # for x in i:
                #        if x != str:
                #            print(x)
                #    if x != 0:
                        # 
#print(first_order)

# print(total_orders)