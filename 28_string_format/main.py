animal = "cow"
item = "moon"
print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) # positional argument
print("The {an} jumped over the {it}".format(an="cow", it="moon")) # keyword argument
print("The {an} jumped over the {an}".format(an="cow", it="moon")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item ))

name = "Alex"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number))
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2))
print("The number pi is {:o}".format(number2))
print("The number pi is {:x}".format(number2))
print("The number pi is {:X}".format(number2))
print("The number pi is {:e}".format(number2))
print("The number pi is {:E}".format(number2))

