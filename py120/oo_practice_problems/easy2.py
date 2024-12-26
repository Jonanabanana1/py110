import os

os.system("clear")


# Suppose you have these two classes:
class Game:
    count = 0

    def __init__(self, name) -> None:
        self.name = name
        Game.count += 1

    def play(self):
        return f"Start the {self.name} game!"


class Bingo(Game):
    def __init__(self, name, player_name) -> None:
        super().__init__(name)
        self.player_name = player_name


class Scrabble(Game):
    def __init__(self, name, player_name1, player_name2) -> None:
        super().__init__(name)
        self.player_name1 = player_name1
        self.player_name2 = player_name2


# # Update this code so that Bingo inherits the play method from the Game class.

# # Update your code from the previous question so the following code works as indicated:
# bingo = Bingo("Bingo", "Bill")
# print(Game.count)  # 1
# print(bingo.play())  # Start the Bingo game!
# print(bingo.player_name)  # Bill

# scrabble = Scrabble("Scrabble", "Jill", "Sill")
# print(Game.count)  # 2
# print(scrabble.play())  # Start the Scrabble game!
# print(scrabble.player_name1)  # Jill
# print(scrabble.player_name2)  # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

# What are the benefits of using object-oriented programming in Python? Think of as many as you can.
"""
1) Modularize code
2) Combine common attributes and functions together into an object
3) Helps solve complex problems
4) Can section off code to help with debugging
"""


# Suppose we have this code:
class Greeting:
    def greet(self, message):
        print(message)


class Hello(Greeting):
    def hi(self):
        super().greet("Hi")


class Goodbye(Greeting):
    def bye(self):
        self.greet("Goodbye")


# Without running the above code, what would each snippet do were you to run it?
"""
hello = Hello()
hello.hi()
"Hello"

hello = Hello()
hello.bye()
Attribute Error

hello = Hello()
hello.greet()
TypeError

hello = Hello()
hello.greet('Goodbye')
Goodbye

Hello.hi()
Type Error, no self is passed to hi()
"""

# Modify the code from the previous question so that Hello.hi() uses the Greeting.greet instance method to print Hi.


# Consider the following code:
class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"I am a {self.type}"


print(Cat("hairball"))
# <__main__.Cat object at 0x10695eb10>
# The output here isn't very useful. It only tells us that we've got an instance of the Cat class, and it's memory address. It would be better if the output were more meaningful. For instance, maybe it can print I am a hairball instead. Update the code to produce that result.


# What would happen if you ran the following code? Don't run it until you've checked your answer:
class Television:
    @classmethod
    def manufacturer(cls):
        return "Amazon"

    def model(self):
        return "Omni Fire"


tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())
