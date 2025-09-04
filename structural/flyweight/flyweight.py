""" Flyweight Design Pattern Implementation """

import random
from abc import ABC, abstractmethod


class Sprite(ABC):
    """ Abstract Sprite class for drawable game objects """

    @abstractmethod
    def draw(self):
        """ Draw the sprite on screen """

    @abstractmethod
    def move(self, x: int, y: int):
        """ Move the sprite to a new position """


class FighterRank:
    """ Enum-like class for Fighter Ranks """
    PRIVATE = 0
    SERGEANT = 1
    MAJOR = 2


class Fighter(Sprite):
    """ Concrete Flyweight object representing a Fighter """

    def __init__(self, rank: FighterRank):
        self.rank = rank

    def draw(self):
        print(f"Drawing fighter of rank {self.rank}")

    def move(self, x: int, y: int):
        print(f"Moving fighter of rank {self.rank} to position {x}, {y}")


class FighterFactory:
    """ Factory to manage Flyweight Fighter objects """

    def __init__(self):
        self._fighters = {}

    def get_fighter(self, rank: FighterRank) -> Fighter:
        """Return existing Fighter if available, else create one."""
        if rank not in self._fighters:
            self._fighters[rank] = Fighter(rank)
        return self._fighters[rank]


class Army:
    """Army class that spawns and manages fighters."""

    def __init__(self, factory: FighterFactory):
        self.factory = factory
        self.army = []

    def spawn_fighter(self, rank: FighterRank):
        """Spawn fighter using Flyweight factory."""
        fighter = self.factory.get_fighter(rank)
        self.army.append(fighter)

    def draw_army(self):
        """Draw representation of the army."""
        for fighter in self.army:
            if fighter.rank == FighterRank.MAJOR:
                print("M ", end="")
            elif fighter.rank == FighterRank.SERGEANT:
                print("S ", end="")
            else:
                print("P ", end="")


if __name__ == "__main__":
    ARMY_SIZE = 500
    factory = FighterFactory()
    army = Army(factory)

    for _ in range(ARMY_SIZE):
        rank = random.randrange(3)
        army.spawn_fighter(rank)

    army.draw_army()
