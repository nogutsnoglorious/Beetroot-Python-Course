# Lesson 10 Homework; Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops(msg):
    raise IndexError(msg)

my_list = [1, 2, 3]

def test_oops():
    try:
        ind = my_list[5]
        print(ind)
    except IndexError as e:
        oops("IndexError is detected!")

test_oops()