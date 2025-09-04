""" Implementation of Chain Of Responsibility """

from __future__ import annotations
from abc import ABC, abstractmethod


class HandlerChain(ABC):
    """ Abstract HandlerChain """
    def __init__(self, input_header: HandlerChain = None):
        self.next_header = input_header

    @abstractmethod
    def add_header(self, input_header: str):
        ...

    def do_next(self, input_header: str):
        if self.next_header:
            return self.next_header.add_header(input_header)
        return input_header


class AuthenticationHeader(HandlerChain):
    """ Authentication HandlerChain to handle authorization tokens """
    def __init__(self, token: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.token = token

    def add_header(self, input_header):
        """ add authorization token """
        h = f"{input_header}\nAuthorization: {self.token}"
        return self.do_next(h)


class ContentTypeHeader(HandlerChain):
    """ ContentType HandlerChain to handle Contenttype headers """
    def __init__(self, content_type: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.content_type = content_type

    def add_header(self, input_header):
        """ add content type header """
        h = f"{input_header}\nContentType: {self.content_type}"
        return self.do_next(h)


class BodyPayloadHandler(HandlerChain):
    """ BodyResponse HandlerChain to handle body response context """
    def __init__(self, body: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.body = body

    def add_header(self, input_header: str):
        """ add body header """
        h = f"{input_header}\n{self.body}"
        return self.do_next(h)


# Usage
if __name__ == "__main__":
    autorization_header = AuthenticationHeader("123456")
    content_type_header = ContentTypeHeader("json")
    body_header = BodyPayloadHandler("Body: {\"Username\":\"John\"}")

    # Passing next handlers of chain
    autorization_header.next_header = content_type_header
    content_type_header.next_header = body_header

    message_with_authentication = autorization_header.add_header("Header with authentication")
    message_without_authentication = content_type_header.add_header("Header without authentication")

    print(message_with_authentication)
    print()
    print(message_without_authentication)
