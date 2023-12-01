# Lesson 14 Homework; Task 3
# Write a decorator "arg_rules" that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed; otherwise, return the result.

from functools import wraps

max_length = 15
should_contain = ['.', '!', 'e']

def validation(a):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            length = True

            # Check for argument length
            # if argument is other type than string, TypeError will raise

            for index, arg in enumerate(args):
                try: 
                    if len(arg) < max_length:
                        for element in should_contain:              # we check if necessary elements are in arguments
                            symbol_check = arg.rfind(element)       
                            if symbol_check != -1:                  # if the element is found we check another argument
                                continue
                            else:
                                return f'{False}\nArgument number {index+1} does not have these symbols: {should_contain}\nOperation execution is impossible.'
                    else:
                        length = False
                        return f'{False}\nLength of argument number {index+1} is more than {max_length}.\nOperation execution is impossible.'
                except TypeError:
                    return f'{False}\nNumber {index+1} argument is not a string object.\nOperation execution is impossible.'
                
            if length == True:
                result = func(*args)
                return result
        return wrapper
    return decorator

arguments = ['Atten!!ti.on.', '!H..el!!!lo.', '!.!fri.en!d']

@validation(max_length)
def sum_strings(*args):
    result = ' '.join(args)
    output_0 = result.replace(should_contain[0], "")
    output = output_0.replace(should_contain[1], "")
    return output

print(sum_strings(*arguments))