from os import system

system("clear")
# Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.
# Modify this class so that the __init__ method optionally lets you specify a fixed banner width when the Banner object is created. The message in the banner should be centered within the banner of that width. Decide for yourself how you want to handle widths that are either too narrow or too wide.

# class Banner:
#     def __init__(self, message, width=-1):
#         self.message = message
#         self.width = width

#     def __str__(self):
#         return "\n".join(
#             [
#                 self._horizontal_rule(),
#                 self._empty_line(),
#                 self._message_line(),
#                 self._empty_line(),
#                 self._horizontal_rule(),
#             ]
#         )

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, width):
#         if width < 0:
#             self._width = len(self.message)
#         else:
#             self._width = width

#     def _empty_line(self):
#         empty_space = " " * self.width
#         return f"| {empty_space} |"

#     def _horizontal_rule(self):
#         dashes = "-" * self.width
#         return f"+-{dashes}-+"

#     def _message_line(self):
#         if self.width <= 0:
#             return f"| {self.message} |"
#         if self.message == "":
#             return f"| {' '.center(self.width)} |"

#         parts = []
#         part = ""
#         for char in self.message:
#             part += char
#             if len(part) == self.width:
#                 parts.append("| " + part + " |")
#                 part = ""
#         if part != "":
#             parts.append(f"| {part.center(self.width)} |")

#         return "\n".join(parts)


# # Comments show expected output
# banner = Banner("To boldly go where no one has gone before.", 10)
# print(banner)
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# banner = Banner("", 40)
# print(banner)
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+


# # Create a Rectangle class whose initializer takes two arguments that represent the rectangle's width and height, respectively. Use the following code to test your solution:
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height


# # Write a class called Square that inherits from the Rectangle class. The Square class is used like this:
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)


# square = Square(5)
# print(square.area == 25)  # True


# # Update this code so you see the following output when you run the code:
# # My cat Cocoa is 3 years old and has black fur.
# # My cat Cheddar is 4 years old and has yellow and white fur.
# class Pet:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age


# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     @property
#     def info(self):
#         return (
#             f"My cat {self.name} is {self.age} "
#             f"years old and has {self.color} fur"
#         )


# cocoa = Cat("Cocoa", 3, "black")
# cheddar = Cat("Cheddar", 4, "yellow and white")

# print(cocoa.info)
# print(cheddar.info)


# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (
#             f"Hello, my name is {self.name} and I am "
#             f"{self.age} years old and {self.status}."
#         )


# class Cat(Animal):
#     def __init__(self, name, age, status, legs=4, species="cat"):
#         super().__init__(name, age, legs, species, status)

#     def introduce(self):
#         return super().introduce() + " Meow Meow!"


# # The Cat initializer should accept 3 parameters: name, age, and status. Cats should always have a leg count of 4 and a species of "cat". The introduce method for the Cat class should return a string identical to the base class with an added Meow meow! at the end. For example:
# cat = Cat("Pepe", 4, "happy")
# expected = "Hello, my name is Pepe and I am 4 years old and happy. Meow Meow!"
# print(cat.introduce() == expected)  # True


# class Dog(Animal):
#     def __init__(self, name, age, status, owner, legs=4, species="dog"):
#         super().__init__(name, age, legs, species, status)
#         self.owner = owner

#     def greet_owner(self):
#         return f"Hi {self.owner}! Woof! Woof!"

#     def introduce(self):
#         return super().introduce() + " Woof! Woof!"


# # The Dog initializer should accept 4 parameters: name, age, status, and owner. Dogs should always have a leg count of 4 and a species of "dog". In addition to the methods inherited from Animal, the Dog class should have a greet_owner method that returns a greeting to its owner followed by Woof! Woof!. The introduce method for the Dog class should return a string identical to the base class with an added Woof! Woof! at the end.
# dog = Dog("Bobo", 9, "hungry", "Daddy")
# expected = (
#     "Hello, my name is Bobo and I am 9 years old " "and hungry. Woof! Woof!"
# )
# print(dog.introduce() == expected)  # True
# print(dog.greet_owner() == "Hi Daddy! Woof! Woof!")  # True


# class Pet:
#     def __init__(self, species, name) -> None:
#         self.species = species
#         self.name = name


# class Owner:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.pet_amount = 0

#     def number_of_pets(self):
#         return self.pet_amount


# class Shelter:
#     def __init__(self) -> None:
#         self.adoptions = {}

#     def adopt(self, owner, pet):
#         self.adoptions.setdefault(owner, [])
#         self.adoptions[owner].append(pet)
#         owner.pet_amount += 1

#     def print_adoptions(self):
#         for owner in self.adoptions:
#             print(f"{owner.name} has adopted the following pets:")
#             for pet in self.adoptions[owner]:
#                 print(f"a {pet.species} named {pet.name}")
#             print()


# # Consider the following code:
# cocoa = Pet("cat", "Cocoa")
# cheddar = Pet("cat", "Cheddar")
# darwin = Pet("bearded dragon", "Darwin")
# kennedy = Pet("dog", "Kennedy")
# sweetie = Pet("parakeet", "Sweetie Pie")
# molly = Pet("dog", "Molly")
# chester = Pet("fish", "Chester")

# phanson = Owner("P Hanson")
# bholmes = Owner("B Holmes")

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} " "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} " "adopted pets.")
# # Write the classes and methods that will be necessary to make this code run, and log the following output:
# # P Hanson has adopted the following pets:
# # a cat named Cocoa
# # a cat named Cheddar
# # a bearded dragon named Darwin

# # B Holmes has adopted the following pets:
# # a dog named Molly
# # a parakeet named Sweetie Pie
# # a dog named Kennedy
# # a fish named Chester

# # P Hanson has 3 adopted pets.
# # B Holmes has 4 adopted pets.


# # Refactor these classes so they all use a common superclass, and inherit behavior as needed.
# class Vehicle:
#     def __init__(self, make, model) -> None:
#         self.make = make
#         self.model = model

#     def info(self):
#         f"{self.make} {self.model}"


# class Car(Vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)

#     def get_wheels(self):
#         return 4


# class Motorcycle(Vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)

#     def get_wheels(self):
#         return 2


# class Truck(Vehicle):
#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

#     def get_wheels(self):
#         return 6


# # You have the following classes.
# class WalkMixin:
#     def walk(self):
#         return f"{self.name} {self.gait()} forward"


# class Person(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"


# class Cat(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"


# class Cheetah(WalkMixin):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"


# # You need to modify the code so that this works:
# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"


# # You may only write one new method to do this.
# # Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently some of our users are nobility, and the regular way of walking simply isn't good enough. Nobility struts.
# # We need a new class Noble that shows the title and name when walk is called. We also require access to name and title; they are needed for other purposes that we aren't showing here.
# class Noble(WalkMixin):
#     def __init__(self, name, title):
#         self.name = name
#         self.title = title

#     def gait(self):
#         return "struts"

#     def walk(self):
#         return f"{self.title} {self.name} {self.gait()} forward"


# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)  # "Byron"
# print(byron.title)  # "Lord"


# Modify the House class so the above program work as shown.
# class House:
#     def __init__(self, price):
#         self.price = price

#     def __lt__(self, other):
#         if not isinstance(other, House):
#             return NotImplemented
#         return self.price < other.price

#     def __gt__(self, other):
#         if not isinstance(other, House):
#             return NotImplemented
#         return self.price > other.price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value


# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")
# # Home 1 is cheaper
# # Home 2 is more expensive


# # Implement a Wallet class that represents a wallet with a certain amount of money. You want to be able to combine (add) two wallets together to get a new wallet with the combined total amount from both wallets.
# # Using the code from the previous exercise, modify the code so that when we print the merged_wallet we receive a message Wallet with $80.
# class Wallet:
#     def __init__(self, amount) -> None:
#         self.amount = amount

#     def __add__(self, other):
#         if not isinstance(other, Wallet):
#             return NotImplemented
#         return Wallet(self.amount + other.amount)

#     def __str__(self):
#         return f"Wallet with ${self.amount}."


# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.amount == 80)  # True
# print(merged_wallet)  # Wallet with $80.


# Write a class such that the following code prints the results indicated by the comments:
class Transform:
    def __init__(self, letters) -> None:
        self.letters = letters

    def uppercase(self):
        return self.letters.upper()

    @classmethod
    def lowercase(cls, word):
        return word.lower()


my_data = Transform("abc")
print(my_data.uppercase())  # ABC
print(Transform.lowercase("XYZ"))  # xyz
