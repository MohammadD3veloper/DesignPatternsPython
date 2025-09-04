""" Interpreter Design Pattern Implementation """

from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    """ Abstract class for expressions """
    @abstractmethod
    def interpret(self):
        """ abstract method for interpret """


# Terminal Expression
class Number(AbstractExpression):
    """ Number class to define Terminal expressions """
    def __init__(self, value):
        self.value = float(value)

    def interpret(self):
        return self.value


# Non-Terminal Expression
class AlgebraExpression(AbstractExpression):
    """ Algebra Expression to define for Non-Terminal Expressions """
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(AlgebraExpression):
    """ Add Expression """
    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(AlgebraExpression):
    """ Subtract Expression """
    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Multiply(AlgebraExpression):
    """ Multiply Expression """
    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Divide(AlgebraExpression):
    """ Divide Expression """
    def interpret(self):
        return self.left.interpret() / self.right.interpret()


# Usage
if __name__ == "__main__":
    TARGET = "3 + 5 - 2 * 7 / 5 + 11"
    tokens = TARGET.split(" ")
    expressions = []

    for c, i in enumerate(range(len(tokens))):
        if i == 0:
            expressions.append(Number(tokens[i]))
        elif tokens[i] == "+":
            expressions.append(Add(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "-":
            expressions.append(Subtract(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "*":
            expressions.append(Multiply(expressions.pop(), Number(tokens[i+1])))
        elif tokens[i] == "/":
            expressions.append(Divide(expressions.pop(), Number(tokens[i+1])))

    result = expressions.pop().interpret()
    print(result)
