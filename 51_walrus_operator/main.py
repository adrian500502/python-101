# walrus operator :=

# happy = True
# print(happy)

# print(happy = True) # won't work like that
print(happy := True) # part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food.upper() == "QUIT" or food.upper() == "Q":
#         break
#     foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

