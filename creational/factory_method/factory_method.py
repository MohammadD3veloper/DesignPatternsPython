""" Factory method Implementation """

from abc import ABC, abstractmethod


class Country:
    """ Country type """

class USA(Country):
    """ USA Country """

class Spain(Country):
    """ Spain Country """


class AbstractCurrencyFactory(ABC):
    """ Abstract Currency Factory class """
    @abstractmethod
    def currency_factory(self, country) -> str:
        """
        our factory method its doing nothing
        just implemented the logic of objects
        """
        raise NotImplementedError


class FiatCurrency(AbstractCurrencyFactory):
    """
    A class that uses AbstractCurrencyFactory to
    implemenet our factory method in real usecase
    In this case its shows fiat currency for each
    country
    """
    def currency_factory(self, country: Country) -> str:
        """
        implemeneted factory method
        
        Args: Country
        Returns: str
        """
        if country is USA:
            return "USD"
        if country is Spain:
            return "EUR"
        else:
            return "IRR"


class VirtualCurrency(AbstractCurrencyFactory):
    """
    A class that uses AbstractCurrencyFactory to
    implemenet our factory method in real usecase
    In this case its shows virtual currency for each
    country (example)
    """
    def currency_factory(self, country):
        """
        implemeneted factory method
        
        Args: Country
        Returns: str
        """
        if country is USA:
            return "Bitcoin"
        elif country is Spain:
            return "Etherium"
        else:
            return "Dodgecoin"


if __name__ == "__main__":
    # Client Usage Step

    f1 = FiatCurrency()
    f2 = VirtualCurrency()

    print(f1.currency_factory(USA))
    print(f2.currency_factory(USA))

    print(f1.currency_factory(Spain))
    print(f2.currency_factory(Spain))
