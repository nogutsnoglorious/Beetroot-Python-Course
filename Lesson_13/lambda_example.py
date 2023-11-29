# lambda arguments : expression
x = lambda a : a + 10
x(7)

y = lambda a, b :a * b
y(8,9)

(lambda x: x + 1)(2)


# comprehensions

len_of_strings = lambda names: [len(x) for x in names]
names = ["Monday", "Tuesday", "Wednesday"]
variable_to_print = len_of_strings(names = names)
print(variable_to_print)


# how to pass function as an argument for another function

def return_len_of_list(list_):
    return len(list_)

def general_func(my_list, return_len_of_list):
    return return_len_of_list


def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def diff(x,y):
    return x-y

def apply_operation(func,x,y):
    return func(x,y)

result_1 = apply_operation(add,3,4)
print("\n", result_1, "\n")

result_2 = apply_operation(multiply,3,4)
print("\n", result_2, "\n")

result_3 = apply_operation(diff,3,4)
print("\n", result_3, "\n")



def general_func(list_):
    def inside():
        print("Saturday")
    inside()