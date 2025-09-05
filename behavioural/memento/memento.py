""" Implementation Memento Design Pattern """

from dataclasses import dataclass


@dataclass
class Memento:
    """ Implementation Memento DataClass """
    state: str


class Originator:
    """
    Implementation Originator class to create Memento and restore it
    Args: state: str
    Returns: None
    """
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        """
        create memento
        Args: None
        Returns: Memento
        """
        return Memento(self.state)

    def restore_memento(self, memento: Memento):
        """
        Restore Memento, restoring the state
        Args: Memento
        Returns: None
        """
        self.state = memento.state



class CareTaker:
    """ CareTaker to manage restore and save states """
    def __init__(self):
        self.memento_list = []

    def save_state(self, state: Memento):
        """
        Save current state to caretaker
        Args: Memento
        Returns: None
        """
        self.memento_list.append(state)

    def restore(self, index: int):
        """
        Restore a state into caretaker
        Args: index: int
        Returns: Memento
        """
        return self.memento_list[index]


# Usage
if __name__ == "__main__":
    originator = Originator("initial-state")
    caretaker = CareTaker()

    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = "state-1"
    caretaker.save_state(originator.create_memento())
    print(f"Current state is : {originator.state}")

    originator.state = "state-2"
    caretaker.save_state(originator.create_memento())
    print(f"Current state is : {originator.state}")

    originator.restore_memento(caretaker.restore(1))
    print(f"Current state is : {originator.state}")

    originator.restore_memento(caretaker.restore(0))
    print(f"Current state is : {originator.state}")

    originator.restore_memento(caretaker.restore(2))
    print(f"Current state is : {originator.state}")
