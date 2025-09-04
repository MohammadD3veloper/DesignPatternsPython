""" Iterator Design Pattern Implementation """

from typing import List, Iterator


class AlphabeticalOrderIterator(Iterator[str]):
    """ Iterator to traverse a collection of words in alphabetical order """

    def __init__(self, collection: List[str], reverse: bool = False):
        self._collection = sorted(collection)
        self._reverse = reverse
        self._position = len(self._collection) - 1 if reverse else 0

    def __iter__(self) -> "AlphabeticalOrderIterator":
        return self

    def __next__(self) -> str:
        if not self._reverse and self._position >= len(self._collection):
            raise StopIteration
        if self._reverse and self._position < 0:
            raise StopIteration

        value = self._collection[self._position]
        self._position += -1 if self._reverse else 1
        return value


class WordsCollection:
    """ A collection of words that provides iterators """

    def __init__(self, collection: List[str]):
        self._collection = list(collection)

    def get_iterator(self) -> AlphabeticalOrderIterator:
        """ Return an iterator in normal alphabetical order """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        """ Return an iterator in reverse alphabetical order """
        return AlphabeticalOrderIterator(self._collection, reverse=True)


# Usage
if __name__ == "__main__":
    words = ["John", "Alex", "Michael", "Carol"]
    collection = WordsCollection(words)

    for word in collection.get_iterator():
        print(word)

    for word in collection.get_reverse_iterator():
        print(word)
