"""
Prototype Pattern Implementation in Python.

Demonstrates how to create independent copies of objects (Prototypes)
using the built-in `copy` library. This allows creating new objects
without directly instantiating their classes.
"""

import copy

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class
    for all shapes
    """
    @abstractmethod
    def draw(self):
        ...


class Square(Shape):
    """ Square shape """
    def __init__(self, size):
        self.size = size

    def draw(self):
        print(f"Drawing a square of size: {self.size}")

class Circle(Shape):
    """ Circle Shap """
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle of radius: {self.radius}")


class AbstractArt:
    """
    Represents an artwork
    consisting of multiple
    shapes
    """
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes

    def draw(self):
        """ draw shapes """
        print(f"Background color is {self.bg_color}")
        for x in self.shapes:
            x.draw()

    def clone(self):
        """Creates and returns a deep copy of the artwork."""
        return copy.deepcopy(self)


if __name__ == "__main__":
    all_shapes = [Square(5), Square(3), Circle(8)]
    art1 = AbstractArt("red", all_shapes)
    art2 = art1.clone() # art2 is Prototype
    art1.draw()
    art2.draw()
