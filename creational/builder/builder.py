""" Builder Implementation """


class NetworkServiceBuilder:
    """
    Builder Network Service
    Handle our multiple parameters
    with __init__ method on python
    and assigning them to object itself
    """
    def __init__(self, url: str = "", auth: str = "", cache: int = 0):
        self.components = {}
        if url:
            self.components['URL'] = url
        if auth:
            self.components['Authorization'] = auth
        if cache:
            self.components['Cache-Control'] = cache

    def show(self):
        """ showing our final component """
        return self.components


if __name__ == "__main__":
    service1 = NetworkServiceBuilder(url="google.com")
    print(service1.show())

    service2 = NetworkServiceBuilder(url="youtube.com", auth="abc123", cache=100000)
    print(service2.show())
