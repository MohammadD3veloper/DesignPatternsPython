""" Implementation Proxy Design Pattern """

from abc import ABC, abstractmethod


class Image(ABC):
    """ Abstract Image class """
    @abstractmethod
    def display(self):
        """ display method to display the given image """


class RealImage(Image):
    """ Class to use it in Proxy class """
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Real image: Loading {filename}")

    def display(self):
        print(f"Real Image: Displaying {self.filename}", end="\n\n")



class ProxyImage(Image):
    """
    Proxy Image to RealImage that can
    handle functionality and acceses to it
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        """
        Proxy display the image method
        
        Args: None
        Returns: None
        """
        print(f"Proxy image: Displaying : {self.filename}")
        if not self.real_image:
            print("From disk")
            self.real_image = RealImage(self.filename)
        else:
            print("From Cache")
        self.real_image.display()


if __name__ == "__main__":
    image = ProxyImage("test.jpg")
    # load image from disk
    image.display()
    # load image from cache
    image.display()
