# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# import module_two
# print(__name__)
# print(module_two.__name__)

def hello():
    print("Hello")

if __name__ == '__main__':
    hello()
    print("Running this module directly")
else: print("Running other module indirectly")
