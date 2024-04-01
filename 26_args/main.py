# *args is a parameter that will pack all arguments into a tuple
# def add(*args):
#     # sum = num1 + num2
#     # return sum
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum

def add(*stuff):
    sum = 0
    # stuff[0] = 0 # Tuples don't support item assignment
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))