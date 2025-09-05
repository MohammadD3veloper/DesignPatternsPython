""" Implementation Mediator Design Pattern """


from __future__ import annotations


class ChatUser:
    """ Implement ChatUser class """
    mediator = None

    def __init__(self, name: str):
        self.name = name

    def set_mediator(self, med: Mediator):
        """ set mediator class """
        self.mediator = med

    def send(self, msg:  str):
        """ send message using mediator class """
        print(f"{self.name} Sending message {msg}")
        self.mediator.send_message(msg, self)

    def recieve(self, msg: str):
        """ Recieve message (Just show) """
        print(f"{self.name} Recieving message {msg}")


class Mediator:
    """ Implement Mediator class """
    users = []

    def add_user(self, user: ChatUser):
        """ add a user to mediator """
        self.users.append(user)
        user.set_mediator(self)

    def send_message(self, msg: str, user: ChatUser):
        """ send message in mediator instead of sender """
        for u in self.users:
            if u != user:
                u.recieve(msg)


# Usage
if __name__ == "__main__":
    mediator = Mediator()
    alice = ChatUser("Alice")
    bob = ChatUser("Bob")
    carol = ChatUser("Carol")

    mediator.add_user(alice)
    mediator.add_user(bob)
    mediator.add_user(carol)

    carol.send("Hi Everyone!")
