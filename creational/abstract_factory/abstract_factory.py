""" Abstract Factory Implementation """

from abc import ABC, abstractmethod
from enum import Enum


class FoodType(Enum):
    """
    A class to declare
    supported food types
    """
    PERSIAN = "persian"
    AMERICAN = "american"


class AbstractRestaurant(ABC):
    """
    A Factory class that implements
    food and drinks on a Restaurant
    """
    @abstractmethod
    def make_food(self):
        """ factory method to make food  """
        raise NotImplementedError

    @abstractmethod
    def make_drink(self):
        """ factory method to make drink """
        raise NotImplementedError


class PersianRestaurant(AbstractRestaurant):
    """
    A Persian Restaurant that inherits from
    RestaurantFactory
    """

    def make_food(self):
        return "GhormeSabzi!"

    def make_drink(self):
        return "doogh Abali"


class AmericanRestaurant(AbstractRestaurant):
    """
    An American Restaurant that inherits from
    RestaurantFactory
    """

    def make_food(self):
        return "Hamburger"

    def make_drink(self):
        return "Coca Cola"


class RestaurantSuggestor:
    """
    A class to suggest restaurant for
    user, it could be a client/user 
    class that using our classes 
    """

    _factory_map = {
        FoodType.PERSIAN: PersianRestaurant,
        FoodType.AMERICAN: AmericanRestaurant
    }

    def __init__(self, food_type: FoodType):
        self.restaurant = None
        self.food_type = food_type

    def suggest_restaurant(self):
        """ Suggest restaurant """
        factory = self._factory_map.get(self.food_type)
        if factory:
            self.restaurant = factory()
        else:
            raise ValueError("Unsupported this type of food")

    def dine(self):
        """ Return the dine menu
        of that restaurant """
        return self.restaurant.make_food(), \
            self.restaurant.make_drink()


if __name__ == "__main__":
    restaurant_1 = RestaurantSuggestor(FoodType.PERSIAN)
    restaurant_1.suggest_restaurant()
    food1, drink1 = restaurant_1.dine()

    restaurant_2 = RestaurantSuggestor(FoodType.AMERICAN)
    restaurant_2.suggest_restaurant()
    food2, drink2 = restaurant_2.dine()

    print("Persian Restaurant:", food1, drink1)
    print("American Restaurant:", food2, drink2)
