# 3. Обчислення вартості доставки:
# Напишіть функцію, яка приймає вагу товару та відстань до місця доставки і обчислює вартість доставки згідно з заданими тарифами.

def send_price(x,y):
    weight_range = 0
    distance_range = 0
    if 0 < x <= 10:
        weight_range = 1
    if 10 < x <= 50:
        weight_range = 3
    elif x > 50:
        weight_range = 5
    if 0 < y <= 50:
        distance_range = 1
    elif 50 < y <= 200:
        distance_range = 2
    elif y>200:
        distance_range = 5
    tarif = x*y*weight_range*distance_range
    print('For your order with weight of {} kg and delivery distance of {} km your price for this service is ${}.'.format(x,y,tarif))



while True:
    weight = input("Enter item's weight: ")
    distance = input("Enter distance to the final destination: ")
    if weight == "" or distance == "":
        print("Okay, bye")
        break
    elif weight.isdigit() and distance.isdigit() and int(weight)>0 and int(distance)>0:
        send_price(int(weight),int(distance))
        break
    else:
        print("Wrong format, try again.")
        continue