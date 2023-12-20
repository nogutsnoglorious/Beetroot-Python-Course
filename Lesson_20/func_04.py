from random import randint

fin_year_1 = [randint(1000,10000) for x in range(4)]
fin_year_2 = [randint(500,3000) for x in range(4)]

def calc_tax(*args, ESV:bool):
    sum_money = sum(args)
    print(sum_money)
    tax_list = ["10%", "20%", "30%"]
    discount = .05* sum_money
    if 0 < sum_money <= 15000:
        tax_payment = sum_money * int(tax_list[0].replace("%",'')) / 100
        return tax_payment
    elif 15000 < sum_money <= 25000:
        if ESV == True:
            tax_payment = sum_money * int(tax_list[1].replace("%",'')) / 100 - discount
            return tax_payment
        else:
            tax_payment = sum_money * int(tax_list[1].replace("%",'')) / 100
            return tax_payment
    elif sum_money > 25000:
        tax_payment = sum_money * int(tax_list[2].replace("%",'')) / 100
        return tax_payment
