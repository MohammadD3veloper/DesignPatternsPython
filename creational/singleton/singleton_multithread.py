""" MultiThread Singleton Pattern Implementation """

from threading import Thread, Lock


class SingletonMultiThread(type):
    """ Simple metaclass
    Instance Manager
    prevents from new
    instance creation """

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class DatabaseDriverThreaded(metaclass=SingletonMultiThread):
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


def connect_db_threaded():
    """
    Instance creation step
    
    Returns:
        object: DatabaseDriver instance obj
    """
    singleton = DatabaseDriverThreaded()
    singleton.connect()
    return singleton


if __name__ == "__main__":
    # Run twice to check new instance creation
    p1 = Thread(target=connect_db_threaded)
    p2 = Thread(target=connect_db_threaded)
    p1.start()
    p2.start()
