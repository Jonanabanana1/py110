import os

os.system("clear")


# Ben and Alyssa are working on a vehicle management system. So far, they have created classes called Auto and Motorcycle to represent automobiles and motorcycles. After having noticed common information and calculations they were performing for each vehicle type, they decided to break the common behaviors into a separate class called WheeledVehicle. This is what their code looks like so far:
class WheelMixin:
    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure


class Vehicle:
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency


class Auto(WheelMixin, Vehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__(50, 25.0)
        self.tires = [30, 30, 32, 32]


class Motorcycle(WheelMixin, Vehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__(80, 8.0)
        self.tires = [20, 20]


# Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:
class Catamaran(Vehicle):
    def __init__(
        self,
        number_propellers,
        number_hulls,
        kilometers_per_liter,
        liters_of_fuel_capacity,
    ):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls

    # ... code omitted ...


# This new class does not fit well with the object hierarchy defined so far. Catamarans don't have tires. But we still want a common code to track fuel efficiency and range. Modify the class definitions and move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.


# Building on the prior question, we now must also track a basic motorboat. A motorboat has a single propeller and hull, but otherwise behaves similar to a catamaran. Therefore, creators of Motorboat instances don't need to specify number of hulls or propellers. How would you modify the vehicles code to incorporate a new Motorboat class?
class Motorboat(Vehicle):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.number_propellers = 1
        self.number_hulls = 1
