""" Command Design Pattern Implementation """

from abc import ABC, abstractmethod


class Command(ABC):
    """ Abstract Command """
    def __init__(self, command_id: int):
        self.command_id = command_id
    @abstractmethod
    def execute(self):
        ...


class OrderAddCommand(Command):
    """ Order Add Command """
    def execute(self):
        print(f"Adding order with id: {self.command_id}")


class OrderPayCommand(Command):
    """ Order Pay Command """
    def execute(self):
        print(f"Paying for order with id : {self.command_id}")


class CommandProcessor:
    """ Command Processor to Process commands in queue """ 

    def __init__(self):
        self.queue = []

    def add_to_queue(self, command: Command):
        """ add a new command to queue """
        self.queue.append(command)

    def process_commands(self):
        """ Process all commands in queue """
        for item in self.queue:
            item.execute()
        self.queue.clear()


# Usage
if __name__ == "__main__":
    processor = CommandProcessor()
    processor.add_to_queue(OrderAddCommand(1))
    processor.add_to_queue(OrderAddCommand(2))
    processor.add_to_queue(OrderPayCommand(1))
    processor.add_to_queue(OrderPayCommand(2))
    processor.process_commands()
