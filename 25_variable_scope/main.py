name = "Alex" # global variable scope

def display_name():
    name = "Williams" # local scope variable
    print(name)

display_name()
print(name)