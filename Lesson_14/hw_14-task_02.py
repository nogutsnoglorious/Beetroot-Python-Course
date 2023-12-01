# Lesson 14 Homework; Task 2
# Write a decorator that takes a list of stop words
# and replaces them with * inside the decorated function

from functools import wraps

def good_sentence(stop_words):
    def decorator(func):
        @wraps(func)
        def wrapper(x):
            print(f'Original sentence is: {func(x)}')                  
            sentence = func(x).split()                                   # tranform our sentence into a list
            for index, word in enumerate(sentence):
                if word in stop_words:
                    sentence[index] = "*"                                # substitute stop words with * in our list
            result = "Edited sentence is: " + " ".join(sentence)         # transforming obtained list into a sentence
            return result
        return wrapper
    return decorator

stop_words = ['shit', 'damn']

@good_sentence(stop_words)
def bad_sentence(x):
    return x

to_say = 'God damn I have just stepped into shit'

print(bad_sentence(to_say))
