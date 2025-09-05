""" Implementation Observer Design Pattern """


from abc import ABC, abstractmethod


class EventListener(ABC):
    """ Implememnts Abstract EventListener class """
    @abstractmethod
    def update(self, event_type: str, file):
        """ abstract update method """


class EventManager:
    """
    Event Manager class

    Args: list[operations]
    Returns: None
    """
    def __init__(self, operations: list):
        self.operations = operations
        self.listeners = {}
        for op in self.operations:
            self.listeners[op] = []

    def subscribe(self, event_type: str, listener: EventListener):
        """ Subscribe to event manager """
        users = self.listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener: EventListener):
        """ Unsubscribe from event manager """
        users = self.listeners[event_type]
        users.remove(listener)

    def notify(self, event_type, file):
        """ send notification to listeners """
        users = self.listeners[event_type]
        for u in users:
            u.update(event_type, file)


class Editor:
    """ Implements Editor class """
    events = EventManager(["open", "save"])
    file = None

    def open_file(self, file):
        """ open file and call notify from event manager """
        self.file = file
        print(f"Editor: Opening file {file}")
        self.events.notify("open", file)

    def save_file(self):
        """ save file and call notify from event manager """
        print(f"Editor: Saving file {self.file}")
        self.events.notify("save", self.file)


class EmailNotificationListener(EventListener):
    """ Implement Notification Listener """
    def __init__(self, email):
        self.email = email

    def update(self, event_type: str, file):
        """ Recieve notifications from event manager """
        print(f"Email to {self.email}: Someone has performed"\
              f" event type: {event_type} operation on the file : {file}")



class LogOpenListener(EventListener):
    """ Implements LogOpen Listener """
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type, file):
        """ Recieve Opened logs notification from event manager """
        print(f"Save to log {self.log_file} Someone has performed"\
              f" {event_type} operation on the file {file}")


# Usage
if __name__ == "__main__":
    editor = Editor()

    email_listener = EmailNotificationListener("test@gmail.com")
    log_listener = LogOpenListener("log.log")

    editor.events.subscribe("open", log_listener)
    editor.events.subscribe("save", log_listener)
    editor.events.subscribe("save", email_listener)

    editor.open_file("log_new.log")
    editor.save_file()
