""" Singleton Pattern Implementation """


class Singleton(type):
    """
    Simple metaclass
    Instance Manager
    prevents from new
    instance creation
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseDriver(metaclass=Singleton):
    """ A sample of database driver
    It should use just one instance
    cause of resource cannot handle
    more than one instance, so we use
    our singleton metaclass """

    def connect(self):
        """
        prints the instance 

        Returns:
            object: DatabaseDriver instance obj (self)
        """
        print(self)


def connect_db():
    """
    Instance creation step
    
    Returns:
        object: DatabaseDriver instance obj
    """
    singleton = DatabaseDriver()
    singleton.connect()
    return singleton

if __name__ == "__main__":
    # Run twice to check new instance creation
    connect_db()
    connect_db()
