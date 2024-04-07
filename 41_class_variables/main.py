from car import Car

car1 = Car("Chevy", "Corvette", 2021, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")

# car1.wheels = 2

Car.wheels = 2
print(Car.wheels)
print(car1.wheels)
print(car2.wheels)
