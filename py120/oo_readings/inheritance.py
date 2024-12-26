"""
# For each of the following pairs of classes, try to determine whether they have an "is-a" or "has-a" relationship or neither.
# First Class 	Second Class
# Car 	        Engine      has-a
# Teacher 	    Student     has-a
# Flag 	        Color       has-a
# Apple 	    Orange      neither
# Ship 	        Vessel      is-a
# Structure 	Home        is-a
# Shape 	    Circle      is-a


# Write the code needed to make the following code work as shown:
class SignalMixin:
    def signal_off(self):
        print("Signal is now off")

    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signalling right")


class Vehicle:
    amount = 0

    def __init__(self) -> None:
        Vehicle.amount += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.amount


class Car(SignalMixin, Vehicle):
    def __init__(self) -> None:
        super().__init__()


class Truck(SignalMixin, Vehicle):
    def __init__(self) -> None:
        super().__init__()


class Boat(Vehicle):
    def __init__(self) -> None:
        super().__init__()


print(Car.vehicles())  # 0
car1 = Car()
print(Car.vehicles())  # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())  # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())  # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())  # 8

# Create a mix-in for the Car and Truck classes from the previous exercise that lets you operate the turn signals: signal left, signal right, and signal off. Use the following code to test your code.

# car1.signal_left()       # Signalling left
truck1.signal_right()  # Signalling right
car1.signal_off()  # Signal is now off
truck1.signal_off()  # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

# Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.
print(Car.mro())
print(type.mro(Truck))
print(type.mro(Boat))
print(type.mro(Vehicle))
"""


# We've provided new Car and Truck classes and some tests below. Refactor them to use inheritance for as much behavior as possible. The tests shown in the code should still work as shown:
class Vehicle:
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg


class Car(Vehicle):

    def family_drive(self):
        print("Taking the family for a drive")


class Truck(Vehicle):

    def hookup_trailer(self):
        print("Hooking up trailer")


car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)
print(Car.mro())
print(car.max_range_in_miles())  # 317.5
print(truck.max_range_in_miles())  # 937.5

car.family_drive()  # Taking the family for a drive
truck.hookup_trailer()  # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print("No family_drive method for Truck")
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print("No hookup_trailer method for Car")
# No hookup_trailer method for Car
