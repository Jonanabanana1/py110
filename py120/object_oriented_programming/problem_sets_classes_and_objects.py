import os

os.system("clear")
# Given the following code, create the Person class needed to make the code work as shown:
# Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.
# Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. Use the following code to test your code:
# Using the class definition from problem 3, let's create some more people (Person objects):
# Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?


class Person:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, other):
        parts = other.strip().split()

        if len(parts) > 1:
            self.last_name = parts[1]
        else:
            self.last_name = ""
        self.first_name = parts[0]

    def __str__(self):
        return self.name


bob = Person("Robert Smith")
rob = Person("Robert Smith")
print(bob.name == rob.name)
