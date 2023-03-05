"""a class that represents a dice"""

from random import randint

class Die:
    """a dice"""

    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self):
        """roll the dice"""
        print(randint(1, self.sides))
