# 3. Обчислення вартості доставки:
# Напишіть функцію, яка приймає вагу товару та відстань до місця доставки і обчислює вартість доставки згідно з заданими тарифами.

def send_price(x,y):
    weight_range = 0
    distance_range = 0

    if x == 0 or y == 0:
        return "Error"
    
    if 0 < x <= 10:
        weight_range = 1
    elif 10 < x <= 50:
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
    return tarif
