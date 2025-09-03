# DesignPatternsPython

We covered 3 types of design patterns (in python language)

1. Creational
2. Structural
3. Behavioural


## Creational
Patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation

### Singleton
Ensures a class has only one instance and provides a global access point to it. Commonly used for shared resources such as databases, loggers, or network connections

PROS:

* Controlled access to shared resources

* Reduced memory footprint (only one instance)

* Consistent state across system

CONS:

* Breaks Single Responsibility Principle (SRP)

* Harder to test (hidden dependencies)

* State persists for application lifetime

Output of singleton.py:
```
$ uv run singleton.py 
<__main__.DatabaseDriver object at 0x1022e35f0>
<__main__.DatabaseDriver object at 0x1022e35f0>
```

Output of singleton_multithread.py
```
$ uv run python singleton_multithread.py
<__main__.DatabaseDriverThreaded object at 0x102ca7350>
<__main__.DatabaseDriverThreaded object at 0x102ca7350>
```

### Factory Method

A method that provides a separation between the client (user) and the actual object creation

* The client only calls the factory method.

* The concrete factory class decides which product (object) to instantiate.

* This hides the creation logic from the client

PROS:
* Requirements change
* Dynamic Switching    
* Seperation of Concern

CONS:
* Increased complexity
* More class and abstraction

Output of factory_method.py
``` 
$ uv run factory_method.py 
USD
Bitcoin
EUR
Etherium
```
### Abstract Factory
It's one level above of the Factory Method; instead of creating a single product, it can create multiple related products
it dosen't directly create objects itself,
but rather acts as a factory of factories

PROS:
* provides a way to access functionality without caring about implementation
* Seperation of concerns
* Allows for testability
* Consistency in related products

CONS:
* Increased Complexity
* Difficult to add a new product of families
    (all concrete factories must be updated)

quivalent:
Factory method: creates a single object
Abstract Factory: creates a family of related objects

Output of abstract_factory.py
```
$ uv run abstract_factory.py 
Persian Restaurant: GhormeSabzi! doogh Abali
American Restaurant: Hamburger Coca Cola
```

### Builder
Used to construct complex objects step by step, especially when objects have many optional or required parameters.
Separates the construction of an object from its representation, allowing the same construction process to create different representations.

PROS:
* Clarity
* Immutability
* Flexibility
* Separation of concerns

CONS:
* More code
* Overkill for simple objects
* Harder to trace/debug

Output of builder.py (classic_builder.py has same output)
```
$ uv run creational/builder/builder.py
{'URL': 'google.com'}
{'URL': 'youtube.com', 'Authorization': 'abc123', 'Cache-Control': 100000}
```

### Prototype
Used when you need to copy an existing object without depending on its concrete class
The copied object must provide proper cloning implementation
Useful in testing, pre-production or when object creation is expensive

PROS:
* Avoids subclassing for creating copies
* Improves performance by reusing existing objects
* Dynamic object creation at runtime

CONS:
* Shallow copies may lead to shared references
* Objects must provide proper cloning implementation
* May increase complexity if object graph is deep
* Tight coupling

output of prototype.py:
```
uv run prototype.py 
Background color is red
Drawing a square of size: 5
Drawing a square of size: 3
Drawing a Circle of radius: 8
Background color is red
Drawing a square of size: 5
Drawing a square of size: 3
Drawing a Circle of radius: 8
```

## Structural
Patterns that focus on how classes and objects are composed to form larger structures, improving flexibility, testability, and scalability

### Adapters
The Adapter is a structural design pattern that makes two incompatible classes work together.
It is especially useful when you cannot or do not want to modify the existing classes

PROS:
* Reuse existing code without modification
* Improves flexibility when integrating with third-party or legacy code
* Separates concerns — client doesn’t need to know about underlying incompatible code
* Makes systems more extensible with multiple adapters

CONS:
* Adds extra complexity and classes to the system
* Too many adapters may make the architecture harder to maintain
* Can reduce performance slightly due to the additional indirection

output of adapter.py:
```
uv run adapter.py
3rd party functionality 2.0 - 2
3rd party functionality 3.0 - 2
3rd party functionality 2.0 - 5
3rd party functionality 6.0 - 1
```

## Behavioural
Patterns that define how objects and classes interact and distribute responsibility
