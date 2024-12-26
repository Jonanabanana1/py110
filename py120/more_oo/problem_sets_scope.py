import os

os.system("clear")


# Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.
# Add a get_breed method to the Dog class from your answer to the previous problem. The method should return the dog's breed. Use the method to print the breeds of the two dog objects you created in the previous problem. You should also mark the breed instance variable for internal use only.
class Dog:
    def __init__(self, breed) -> None:
        self._breed = breed

    def get_breed(self):
        return self._breed


# poodle = Dog("Poodle")
# golden_retriever = Dog("Golden Retriever")
# print(poodle.get_breed())
# print(golden_retriever.get_breed())


# Create a Cat class that has a single method named get_name that returns the name instance variable. Without initializing name, try to instantiate a Cat object and call get_name. Print Name not set! when the error occurs.
class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"


# cat = Cat()
# print(cat.get_name())

# Create an instance of the Dog class from your answer to Problem 2. Set its breed directly from outside the class, then print the resulting breed.
# dog3 = Dog("teehee")
# dog3._breed = "bruh"
# print(dog3.get_breed())


# Define a Student class that has a class variable named school_name. You should initialize the school name to 'Oxford'. After defining the class, instantiate an instance of the Student class and print the school name using that instance.
class Student:
    school_name = "Oxford"

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name


# stud = Student()
# print(stud.__class__.school_name)

# Modify the Student class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. Create two Student objects with different names but the same school, then print the name and school for both students.
# tim = Student("Tim")
# jack = Student("Jack")
# print(tim.name)
# print(jack.name)
# print(tim.__class__.school_name)
# print(jack.__class__.school_name)

# Modify the Student class from your answer to the previous problem. The modified class should have a class method that returns the school's name. Without instantiating any Student objects, print the school's name in two different ways: once with the class method, and once by accessing the class variable directly.
# print(Student.get_school_name())
# print(Student.school_name)


# Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer. Initialize these variables to different values. Add a show_manufacturer method that prints both the class and instance variables.
class Car:
    manufacturer = "Tesla"

    def __init__(self) -> None:
        self.manufacturer = "Nissan"

    def show_manufacturer(self):
        print(self.manufacturer, Car.manufacturer)


# Car().show_manufacturer()


# Create a Bird class that has a species attribute. Create a Sparrow class that inherits from the Bird class. Create a Sparrow instance object, then print its species. The expected output is sparrow.
# class Bird:
#     species = "Sparrow"


# class Sparrow(Bird):
#     pass

# spar = Sparrow()
# print(spar.species)


# Consider the following code:
class Bird:
    def __init__(self, species):
        self.species = species


class Sparrow(Bird):
    def __init__(self, species, color):
        # super().__init__(species) # Fix
        self.color = color


# birdie = Sparrow("sparrow", "brown")
# print(birdie.species)  # What will this output?
# Without running the above code, what will it output? If it raises an error, explain why and how to fix it.


# Create a Mammal class that always sets an attribute called legs to a value of 4. Create a Human class that inherits from Mammal, but instead sets the value of legs to 2. Print the number of legs for a human to verify correct operation.
class Mammal:
    def __init__(self) -> None:
        self.legs = 4


class Human(Mammal):
    def __init__(self) -> None:
        self.legs = 2


# print(Human().legs)


# Consider the following code:
class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound


class Lion(Cat):
    sound = "roar"


print(Lion.make_sound())
# What will this code output, and why?
# print 'roar' because the invoke make_sound as Lion as the caller so cls refers to Lion which will use Lion's sound variable


# Consider the following code:
class Tree:
    def __init__(self):
        self.type = "Generic Tree"


class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"


# When an instance of Pine is created, what value will its type attribute have? Why?
# It will be Pine Tree because you are reassigning self.type on the next line after super


# Consider the following code:
class A:
    def __init__(self):
        self.var_a = "A class variable"


class B(A):
    def __init__(self):
        self.var_b = "B class variable"


b = B()


# print(b.var_a)
# Without running this code, what will happen if you were to run it? Why?
# Attribute Error because var_a doesn't exist in class B because you never invoke A's init method
