""" Facade Design Pattern Implementation """

from dataclasses import dataclass


class ComplexSystemStore:
    """ A (may 3rd party) complex system """
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}

    def store(self, key: str, value: str):
        """ store in cache system """
        self.cache[key] = value

    def read(self, key: str) -> str:
        """ read from cache system """
        return self.cache[key]

    def commit(self):
        """ commit data to system store """
        print(f"Storing cache data to file {self.filepath}")


@dataclass
class User:
    """ User data class """
    login: str


class UserRepository:
    """ Facade User Repo class """

    def __init__(self):
        self.system_preference = ComplexSystemStore("./default.prefs")

    def save(self, user: User):
        """ save user facade way to system store """
        self.system_preference.store("USER", user.login)
        self.system_preference.commit()

    def find_first(self):
        """ find user facade way from system store """
        return User(self.system_preference.read("USER"))


if __name__ == "__main__":
    user_repo = UserRepository()
    user = User("John")

    user_repo.save(user)

    retrieved_user = user_repo.find_first()

    print(retrieved_user.login)
