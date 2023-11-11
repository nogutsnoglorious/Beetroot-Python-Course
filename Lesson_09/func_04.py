# 1. Калькулятор податків:
# Напишіть функцію, яка приймає суму доходу і обчислює загальну суму податку, враховуючи різні ставки податків на прибуток.

def tax(x):
    final_tax = 0
    tax_percentage = 0
    if x > 100000:
        tax_percentage = 39
        final_tax = x * tax_percentage/100
    elif 50000 < x < 100000:
        tax_percentage = 20
        final_tax = x * tax_percentage/100
    else:
        tax_percentage = 5
        final_tax = x * tax_percentage/100
    print('Your tax for this year equals {}% with total sum of {}.'.format(tax_percentage,int(final_tax)))

annual_salary = 0
while True:
    salary = input("What is your monthly salary this year? ")
    months = input("For how many months did you work this year? ")
    if salary.isdigit() == False or months.isdigit() == False:
        print("Wrong inputs format. Enter numbers, please")
        continue
    else:
        annual_salary = int(salary) * int(months)
        tax(annual_salary)
        break