import os

os.system("clear")


# Create a Car class that makes the following code work as indicated:
class Car:
    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        return f"{self.color.title()} {self.year} {self.model}"

    def __repr__(self) -> str:
        model = repr(self.model)
        year = repr(self.year)
        color = repr(self.color)
        return f"Car({model}, {year}, {color})"


# vwbuzz = Car("ID.Buzz", 2024, "red")
# print(vwbuzz)  # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

import math


# Earlier, we wrote the following class:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x * other.x) + (self.y * other.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f"Vector({x}, {y})"


# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)  # Vector(18, 8)

# # Update the class so the code below works as intended
# print(v1 - v2)  # Vector(-8, 16)
# print(v1 * v2)  # 17
# print(abs(v1))  # 13.0


# Challenge: Create the classes needed to make the following code work as shown:
class Candidate:
    def __init__(self, name) -> None:
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other
        return self


class Election:
    def __init__(self, candidates) -> None:
        self.candidates = candidates

    def results(self):
        winner_votes = 0
        winner_name = None
        total_votes = 0
        for candidate in self.candidates:
            if candidate.votes > winner_votes:
                winner_votes = candidate.votes
                winner_name = candidate.name
            total_votes += candidate.votes
            print(f"{candidate.name}: {candidate.votes} votes")
        print(
            f"\n{winner_name} won: {winner_votes / total_votes * 100:.1f}% of votes"
        )


mike_jones = Candidate("Mike Jones")
susan_dore = Candidate("Susan Dore")
kim_waters = Candidate("Kim Waters")

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes
