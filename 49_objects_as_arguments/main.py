class Car:
    color = None

# def change_color(car, color):
#     car.color = color

def change_color(vehicle, color):
    vehicle.color = color

class Motorcycle:
    color = None

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()

change_color(car1, "red")
change_color(car2, "white")
change_color(car3, "blue")
change_color(bike1, "black")

print(car1.color, car2.color, car3.color, sep="\n")
print(bike1.color)