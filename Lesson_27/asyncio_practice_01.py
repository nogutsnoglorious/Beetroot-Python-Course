# 1. Створіть дві-три прості функції, які виконують наступні дії:

# Функція 1: Симуляція обробки даних, наприклад, затримка в обробці або обчислення
# (ця функція може "обробляти" велику кількість даних, використовуючи просту затримку. Наприклад, може просто чекати 2 секунди перед завершенням своєї роботи.)

# Функція 2: Генерація певної інформації або структури даних
# (ця функція може створювати та повертати певну структуру даних, наприклад, список чи словник з випадковими значеннями.)

# (Опціонально) Функція 3: Інша корисна дія, яка може бути асинхронною або потоковою. 
# (ця функція може представляти будь-який інший корисний процес, наприклад, сортування списку або конвертацію даних.)

# 2. Реалізуйте ці функції в асинхронному режимі за допомогою asyncio.
# 3. Реалізуйте ці функції в багатопотоковому режимі за допомогою threading.
# 4. Створіть основний скрипт, який демонструє виконання цих функцій в обох режимах.
# 5. Зробіть вимірювання часу виконання для кожної функції в обох режимах.

import math
import time
import asyncio
import threading
from random import randint

# asynchronious

# calculate area of a circle
async def func_01():
    start_time = time.time()
    print("Func 01 has started it's execution.")
    r = randint(1,100)
    A = math.pi*r**2
    await asyncio.sleep(3) 
    end_time = time.time()
    print("Func 01 has ended it's execution.")
    elapsed_time = end_time - start_time
    print(f"Total Func 01 execution time is {round(elapsed_time,3)} sec.")
    return A

# generate list of random numbers and find their sum
async def func_02():
    start_time = time.time()
    print("Func 02 has started it's execution.")
    num_list = [randint(1,1000000) for x in range(1,1000000)]
    num_list_sum = sum(num_list)
    end_time = time.time()
    print("Func 02 has ended it's execution.")
    elapsed_time = end_time - start_time
    print(f"Total Func 02 execution time is {round(elapsed_time,3)} s.")
    return num_list_sum

# generate list of random numbers and sort them in descending order
async def func_03():
    start_time = time.time()
    print("Func 03 has started it's execution.")
    num_list = [randint(1,1000000) for x in range(1,10000)]
    num_list.sort()
    end_time = time.time()
    print("Func 03 has ended it's execution.")
    elapsed_time = (end_time - start_time) * 1000
    print(f"Total Func 03 execution time is {round(elapsed_time,3)} ms.")
    return num_list

async def main():
    await asyncio.gather(
        func_01(),
        func_02(),
        func_03()
    )

asyncio.run(main())

# -------------------------------------

# multithreading

# calculate area of a circle
def mfunc_01():
    start_time = time.time()
    print("MFunc01 has started it's execution.")
    r = randint(1,100)
    A = math.pi*r**2
    time.sleep(3)
    end_time = time.time()
    print("MFunc01 has ended it's execution.")
    elapsed_time = end_time - start_time
    print(f"Total MFunc01 execution time is {round(elapsed_time,3)} sec.")
    return A

# generate list of random numbers and find their sum
def mfunc_02():
    start_time = time.time()
    print("MFunc02 has started it's execution.")
    num_list = [randint(1,1000000) for x in range(1,1000000)]
    num_list_sum = sum(num_list)
    end_time = time.time()
    print("MFunc02 has ended it's execution.")
    elapsed_time = end_time - start_time
    print(f"Total MFunc02 execution time is {round(elapsed_time,3)} s.")
    return num_list_sum

# generate list of random numbers and sort them in descending order
def mfunc_03():
    start_time = time.time()
    print("MFunc03 has started it's execution.")
    num_list = [randint(1,1000000) for x in range(1,10000)]
    num_list.sort()
    end_time = time.time()
    print("MFunc03 has ended it's execution.")
    elapsed_time = (end_time - start_time) * 1000
    print(f"Total MFunc03 execution time is {round(elapsed_time,3)} ms.")
    return num_list

def threads_main():
    threads = []
    
    # Create a thread for each function
    thread_1 = threading.Thread(target=mfunc_01)
    thread_2 = threading.Thread(target=mfunc_02)
    thread_3 = threading.Thread(target=mfunc_03)
    
    # Start the threads
    thread_1.start()
    thread_2.start()
    thread_3.start()
    
    # Append the threads to the list
    threads.append(thread_1)
    threads.append(thread_2)
    threads.append(thread_3)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    threads_main()




