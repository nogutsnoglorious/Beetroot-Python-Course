# 4. Система обліку вартості проекту:
# Напишіть функцію, яка приймає вартість робочих годин, кількість годин та додаткові витрати і розраховує загальну вартість проекту.

def project_estimate(x,y,z,w):
    if w == 0:
        final_price = x*y
        print('Your final project price is {} with no additional services.'.format(final_price))
    else:
        i = add_services.get(z)
        final_price = x*y + i*w
        print('Your final project price is {} with additional services: {}, {} time(s).'.format(final_price, z, w))

while True:
    add_services = {
        "audit": 250,
        "coffee": 10,
        "designer": 500,
        "project manager": 1000
    }
    rate = input("Enter teams work rate: ")
    hours = input("Enter teams approximate total hour load: ")
    q1= input(f'Here is a list of additional services: {add_services}, would you like to choose something?: ')
    if rate.isdigit() and hours.isdigit() and q1 == "":
        print("Okay, let's calculate your project price.")
        project_estimate(int(rate),int(hours),0,0)
        break
    elif rate == "" or hours == "" or q1 == "":
        print("Okay, bye")
        break
    else:
        service_question = input("Enter desired additional service: ")
        service_quantity = input("Enter quantity of chosen service: ")
        if rate == "" or hours == "" or service_question == "" or service_quantity == "":
            print("Okay, bye")
            break
        elif rate.isdigit() and hours.isdigit() and service_quantity.isdigit() and int(rate)>0 and int(hours)>0 and int(service_quantity)>0:
            project_estimate(int(rate),int(hours),service_question,int(service_quantity))
            break
        else:
            print("Oops, there's an error. Try again.")
            continue