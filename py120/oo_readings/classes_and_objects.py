import os
import pdb

os.system("clear")
# Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.
# class Person:
#     def __init__(self, name) -> None:
#         self.name = name


# timothy = Person("Timothy")
# hogan = Person("Hogan")


# Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.
class Foo:
    pass


foo = Foo()
# print(f"I am a {type(foo).__name__} object")
# print(f"I am a {foo.__class__.__name__} object")

# Create a Car class that meets these requirements:

# Each Car object should have a model, model year, and color provided at instantiation time.
# You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
# Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
# Create a method that prints a message about the car's current speed.
# Write some code to test the methods.


class Car:
    def __init__(self, model: str, year: int, color: str) -> None:
        self._model = model
        self._year = year
        self.color = color
        self._speed = 0

    @staticmethod
    def average_gas_mileage(miles, gallons):
        mileage = miles / gallons
        print(
            f"Average gas mileage traveling {miles} miles"
            f" in {gallons} gallons is {mileage:.2f} miles per gallon."
        )

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color) -> None:
        if not isinstance(color, str):
            raise ValueError("Color must be a string")
        self._color = color

    def engine_on(self) -> None:
        print("Turning on the engine!")

    def engine_off(self) -> None:
        self._speed = 0
        print("Turning off the engine!")

    def brake(self) -> None:
        print("Braking!")
        if self._speed != 0:
            self._speed -= 10

    def accelerate(self, number) -> None:
        self._speed += number
        print(f"Accelerating {self._speed} mph!")

    def get_speed(self) -> None:
        print(f"Current speed is {self._speed} mph.")

    def paint(self, color) -> None:
        self.color = color
        print(f"Spray painting car {color}")


nissan = Car("Nissan", 2016, "red")
# nissan.engine_on()
# nissan.get_speed()
# nissan.accelerate(20)
# nissan.get_speed()
# nissan.brake()
# nissan.get_speed()
# nissan.engine_off()

# Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.
# nissan.color = "blue"
# print(nissan.color)

# Add a method to the Car class that lets you spray paint the car a specific color. Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.
# nissan.paint("green")

# Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).
# Car.average_gas_mileage(100, 20)


# Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.
# The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.
# The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.


class Person:
    def __init__(self, first_name, last_name) -> None:
        Person.validate_name((first_name, last_name))
        self._first_name = first_name
        self._last_name = last_name

    @staticmethod
    def validate_name(name: tuple):
        first_name, last_name = name
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Name must be a string")
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("Name must consist of alphabetic characters only")

    @property
    def name(self):
        return f"{self._first_name.title()} {self._last_name.title()}"

    @name.setter
    def name(self, name):
        Person.validate_name(name)
        self._first_name, self._last_name = name
