""" Builder Implementation """

class NetworkService:
    """
    NetworkService object
    Used in builder to build
    object of it
    """
    def __init__(self):
        self.components = {}

    def add(self, key: str, value: str):
        """ add new component """
        self.components[key] = value

    def show(self):
        """ show components """
        return self.components


class NetworkServiceBuilder:
    """
    Builder class of NetworkService
    Creates objects of NetworkService
    using classic way of builder pattern
    """
    def __init__(self):
        self._service = NetworkService()

    def add_target_url(self, url: str):
        """ add url parameter to service """
        self._service.add("URL", url)
        return self

    def add_auth(self, auth: str):
        """ add auth parameter to service """
        self._service.add("Authorization", auth)
        return self

    def add_caching(self, cache: int):
        """ add caching parameter to service """
        self._service.add('Cache-Control', cache)
        return self

    def build(self) -> NetworkService:
        """
        used to build object
        Returns: NetworkService
        """
        service = self._service
        self._service = NetworkService()
        return service


if __name__ == "__main__":
    # Usage of builder
    builder = NetworkServiceBuilder()
    # Service 1
    builder.add_target_url("google.com")
    service1 = builder.build()
    print(service1.show())

    # Service 2
    builder.add_target_url("youtube.com").add_auth("abc123").add_caching(100000)
    service2 = builder.build()
    print(service2.show())
