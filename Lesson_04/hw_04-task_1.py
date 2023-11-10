while True:
    word = input("Enter a desired word (f.e. 'helloworld', 'my', 'x', etc): ")
    if word == "":
        break
    elif len(word) >= 2:
        print(word[:2] + word[-2:])
    else:
        print("")
 



# early version of code

"""
# held
sample_1 = 'helloworld'
print(sample_1[:2]+sample_1[-2:])

# mymy
sample_2 = 'my'
print(sample_2[:2]+sample_2[-2:])

# empty string
sample_3 = 'x'
if len(sample_3) < 2:
    print("")
"""