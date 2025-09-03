""" Adapter Design Pattern Implementation """

from dataclasses import dataclass
from typing import List


@dataclass
class DisplayDataType:
    """Represents the display data format (3rd-party)."""
    index: float
    data: str


class DisplayData:
    """
    A 3rd-party class that we want to adapt
    to work with other data sources.
    """
    def __init__(self, display_data: DisplayDataType):
        self.display_data = display_data

    def show_data(self) -> None:
        """Simulates showing data on a display."""
        print(f"3rd party functionality {self.display_data.index} - {self.display_data.data}")


@dataclass
class DatabaseDataType:
    """Represents the database data format (3rd-party)."""
    position: int
    amount: int


class StoreDatabaseData:
    """
    Another 3rd-party class representing
    a database storage system.
    """
    def __init__(self, database_data: DatabaseDataType):
        self.database_data = database_data

    def store_data(self) -> None:
        """Simulates storing data in a database."""
        print(f"Database data stored: {self.database_data.position} - {self.database_data.amount}")


class DisplayDataAdapter:
    """
    Adapter class that makes DatabaseDataType
    compatible with DisplayData.
    """
    def __init__(self, db_data: List[DatabaseDataType]):
        self.db_data = db_data

    def store_data(self) -> None:
        """Adapts database data to display format and prints it."""
        for item in self.db_data:
            ddt = DisplayDataType(float(item.position), str(item.amount))
            display = DisplayData(ddt)
            display.show_data()


def generate_data() -> List[DatabaseDataType]:
    """Sample data generator for demonstration."""
    return [
        DatabaseDataType(2, 2),
        DatabaseDataType(3, 2),
        DatabaseDataType(2, 5),
        DatabaseDataType(6, 1),
    ]


if __name__ == "__main__":
    adapter = DisplayDataAdapter(generate_data())
    adapter.store_data()
