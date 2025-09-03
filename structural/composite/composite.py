""" Composite design pattern Implementation """

from abc import ABC, abstractmethod

class Component(ABC):
    """Base class for Equipment and Composite"""

    @property
    @abstractmethod
    def price(self):
        """Return the price of the component"""


class Equipment(Component):
    """Leaf node in the tree"""

    def __init__(self, name: str, price: int):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price


class Composite(Component):
    """Composite node, can contain Equipment or other Composites"""

    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, component: Component):
        """Add a component (leaf or composite)"""
        self.items.append(component)
        return self

    @property
    def price(self):
        """Calculate total price of all children"""
        return sum(item.price for item in self.items)


# Usage
if __name__ == "__main__":
    # Create components
    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Hard Drive", 250)
    rom = Equipment("ROM", 100)
    ram = Equipment("RAM", 75)

    # Create composites
    memory = Composite("Memory").add(rom).add(ram)
    computer = Composite("PC").add(processor).add(hard_drive).add(memory)

    print(f"Total price of PC: {computer.price}")
