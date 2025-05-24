"""
P:Create a robot factory that generates robots with random names
The random names should be in this format:
    XX123 - 2 Random capital alpha letters, followed by 3 random numbers

Create a class named Robot that contains a name property and a reset instance method. The reset instance method should reset and create a new robot name.

A robot's name is created whenever a robot instance is instantiated, or reset is called.

Robot must not have the same name as other robots made in the factory so keep generated names saved inside of a set.

Ideas:
    - import random module to randomly generate letter/number
    - Do this 2 times each for letter/number and append each time to name to get full name
    - Store this in a helper generate name method
    - Each time name is generated store name in a set stored by the class


"""

import random
from string import ascii_uppercase


class Robot:
    old_names = set()

    def __init__(self) -> None:
        self.name = Robot.generate_rand_name()

    @classmethod
    def generate_rand_name(cls) -> str:
        while True:
            letters = "".join(random.choice(ascii_uppercase) for _ in range(2))
            numbers = "".join(str(random.randint(0, 9)) for _ in range(3))

            new_name = letters + numbers
            if new_name not in cls.old_names:
                cls.save_name(new_name)
                return new_name

    @classmethod
    def save_name(cls, name: str) -> None:
        cls.old_names.add(name)

    def reset(self) -> None:
        self.name = Robot.generate_rand_name()
