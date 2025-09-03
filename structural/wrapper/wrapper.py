""" Implementation of Wrapper (Decorator) Design Pattern """

from abc import ABC, abstractmethod


class CoffeeMachine(ABC):
    """Abstract base class representing a Coffee Machine from a third-party library."""

    @abstractmethod
    def make_small_coffee(self):
        """Prepare a small coffee"""
        ...

    @abstractmethod
    def make_large_coffee(self):
        """Prepare a large coffee"""
        ...


class BasicCoffeeMachine(CoffeeMachine):
    """A basic coffee machine implementing the CoffeeMachine interface."""

    def make_small_coffee(self):
        print("Basic CoffeeMachine making small coffee")

    def make_large_coffee(self):
        print("Basic CoffeeMachine making large coffee")


class EnhancedCoffeeMachine(CoffeeMachine):
    """
    Wrapper / Decorator class to extend the functionality of BasicCoffeeMachine.
    It can override existing methods or add new features.
    """

    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    def make_small_coffee(self):
        """Delegates to the original small coffee method"""
        self.basic_machine.make_small_coffee()

    def make_large_coffee(self):
        """Overrides the original large coffee method"""
        print("Enhanced Coffee Machine making large coffee")

    def make_milk_coffee(self):
        """Adds a new feature: making milk coffee"""
        print("Enhanced coffee machine making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enhanced coffee machine adding milk")


# Usage
if __name__ == "__main__":
    basic_machine = BasicCoffeeMachine()
    enhanced_machine = EnhancedCoffeeMachine(basic_machine)

    enhanced_machine.make_small_coffee()
    enhanced_machine.make_large_coffee()
    enhanced_machine.make_milk_coffee()
