import os

os.system("clear")
# Update the following code so that, instead of printing the values, each statement prints the name of the class to which it belongs.

# Comments show expected output
# print("Hello".__class__)  # <class 'str'>
# print(type(5))  # <class 'int'>
# print([1, 2, 3].__class__)  # <class 'list'>


# Create an empty class named Cat.


# Using the code from the previous exercise, create an instance of Cat and assign it to a variable named kitty.
# kitty = Cat()

# Using the code from the previous exercise, add a __init__ method that prints I'm a cat! when a new Cat object is instantiated.

# Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

# Using the code from the previous exercise, move the greeting from the __init__ method to an instance method named greet that prints a greeting when invoked. Make sure you write some code that invokes the method.

# Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

# Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.


# Using the code snippet provided below, add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again.
class Cat:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, other):
        self._name = other

    def greet(self):
        print(f"{self.name} says hi!")


# kitty = Cat("Sophie")
# kitty.greet()
# kitty.name = "Luna"
# kitty.greet()


# Create a class named Person.
# When you instantiate a Person object, you should pass in one argument that contains the person's name.
# If no arguments are given, the Person object should be instantiated with a name of "John Doe".
class Person:
    def __init__(self, name="John Doe") -> None:
        self.name = name


person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)  # John Doe
print(person2.name)  # Pepe Le Pew
