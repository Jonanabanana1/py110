import os

os.system("clear")
# Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?
# True                          bool object
# 'hello'                       str obj
# [1, 2, 3, 'happy days']       list obj
# 142                           int obj
# {1, 2, 3}                     set obj
# 1.2345                        float obj
# You can do obj.__class__ to find what obj they belong to or type(obj)


# Suppose you have an AngryCat class that looks like this:
class AngryCat:
    def hiss(self):
        print("Hisssss!!!")


# How would you create a new instance of this class?
cat = AngryCat()


# If we have a Car class and a Truck class and we want to be able to go_fast, how can we add the ability for them to go_fast using the mix-in SpeedMixin? How can you check whether your Car or Truck can now go fast?
class SpeedMixin:
    def go_fast(self):
        print(f"I am a super fast {self.__class__.__name__}")


class Car(SpeedMixin):
    def go_slow(self):
        print("I am safe and driving slow.")


class Truck(SpeedMixin):
    def go_very_slow(self):
        print("I am a heavy truck and like going very slow.")


print(hasattr(Truck, "go_fast"))
print(hasattr(Car, "go_fast"))

# When we called small_car.go_fast, you may have noticed that the output includes the vehicle type. How is this done?
# self.__class__ refers to the calling object's class which in this case would be an object of the Car class


# Which of the following classes would create objects that have an instance variable. How do you know?
class Fruit:
    def __init__(self, name):
        my_name = name


class Pizza:
    def __init__(self, name):
        self.my_name = name


# The pizza class would create an instance variable as it has self. before the variable name

# Without running the following code, can you determine what the following code will do? Explain why you will get those results.
import random


class Oracle:
    def predict_the_future(self):
        return f"You will {random.choice(self.choices())}."

    def choices(self):
        return [
            "eat a nice lunch",
            "take a nap soon",
            "stay at work late",
            "adopt a cat",
        ]


oracle = Oracle()
print(oracle.predict_the_future())
# Will print "You will ..." where ... is a random element given by the return list in choices


class RoadTrip(Oracle):
    def choices(self):
        return [
            "visit Vegas",
            "fly to Fiji",
            "romp in Rome",
            "go on a Scrabble cruise",
            "get hopelessly lost",
        ]


# What will happen when you run the following code?
# trip = RoadTrip()
# print(trip.predict_the_future())
# Will print one of the string choices in RoadTrip's choices method as it overrides the superclass' choices functions

# Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient.
# Use my_obj.__class__.mro()

# There are several variables listed below. What are the different variable types and how do you know which is which?
# excited_dog = "excited dog"                        local/global variable
# self.excited_dog = "excited dog"                   instance variable
# self.__class__.excited_dog = "excited dog"         class variable
# BigDog.excited_dog = "excited dog"                 Property


# Suppose you have the following class:
class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count


# Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.
# _cats_count keeps track of how many instances of Cat has been initialized
cat1 = Cat("poop")
cat2 = Cat("doop")
print(Cat.cats_count())
