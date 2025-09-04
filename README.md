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

### Bridge
The Bridge is an abstraction from its implementation so that the two can vary independently.
It’s especially useful when you have multiple orthogonal hierarchies (e.g., different
devices and different types of remotes) and want to avoid a combinatorial explosion of classes.

Key Idea:
Instead of creating subclasses for every possible combination of abstraction and implementation, you bridge them via composition.

PROS
* Decouples abstraction from implementation → easier to extend both independently
* Increases flexibility and scalability
* Improves maintainability (each hierarchy evolves separately)
* Avoids combinatorial class explosion

CONS
* Adds extra complexity with more classes and indirection
* Harder for beginners to understand the relationship between abstraction and implementation
* May be overkill for small/simple hierarchies

Output of bridge.py:
```uv run bridge.py 
Radio <__main__.Radio object at 0x100550110> volume up: 1
Radio <__main__.Radio object at 0x100550110> volume up: 2
Radio <__main__.Radio object at 0x100550110> volume down: 1
TV <__main__.TV object at 0x100550200> volume up: 1
TV <__main__.TV object at 0x100550200> volume down: 0
TV <__main__.TV object at 0x100550200> volume up: 1
TV <__main__.TV object at 0x100550200> volume down: 0
```

### Composite
The Composite pattern allows you to compose objects into tree-like structures to represent part-whole hierarchies.
It lets clients treat individual objects and compositions of objects uniformly, so you can manipulate many objects as a single entity.

Use cases:

Represent hierarchical structures (e.g., file system, organization charts).
Treat single objects and groups of objects in the same way.
Reduce client-side complexity when working with recursive structures.

PROS:
* Simplifies client code by treating individual and composite objects uniformly.
* Makes it easy to add new components.
* Can represent complex hierarchies clearly.

CONS:
* Can make the design more complex if overused.
* Might require careful handling of recursion and tree traversal.
* Equivalent concepts:
* Tree structures in data.
* Polymorphism is often used to allow uniform treatment of leaf and composite nodes.

output of composite.py:
```
$ uv run composite.py
Total price of PC: 1425
```

### Decorator/Wrapper
The Decorator (or Wrapper) pattern is used to extend or modify the behavior of a class without changing its source code.
It is especially useful when dealing with third-party classes or libraries over which you have no control, but you want to alter their functionality or add new features.

Key ideas:   
* Attach new behavior to an object dynamically at runtime.
* Override existing behavior without modifying the original class.
* Respect the Open/Closed Principle — open for extension, closed for modification.
* Can be used for personalization, logging, caching, or security features.

PROS:
* Add new features without modifying original code.
* Combine multiple decorators to build complex functionality.
* Improves code flexibility and reusability.

CONS:
* Increases number of classes and complexity.
* Can make the object graph harder to follow.
* Too many nested decorators can be difficult to debug.
* Usage example: wrapping a basic coffee machine to add milk coffee preparation, while still keeping original small and large coffee functionality intact.

output of wrapper.py:
``` $ uv run wrapper.py
Basic CoffeeMachine making small coffee
Enhanced Coffee Machine making large coffee
Enhanced coffee machine making milk coffee
Basic CoffeeMachine making small coffee
Enhanced coffee machine adding milk
```

### Facade
The Facade design pattern provides a simple interface to a larger body of complex code, such as a library, framework, or subsystem.
It hides internal complexities and exposes only the parts that are necessary for the client.

PROS:
* Hides away complexity behind a single, simple interface
* Provides a clear and unified entry point to complex functionality
* Removes the need for direct object/memory management in the client
* Simplifies client implementation and usage
* Encourages separation of concerns (client doesn’t need to know system details)

CONS:
* Can become a god-object if too much responsibility is centralized
* Risk of reducing flexibility by exposing only limited functionality

output of facade.py:
``` $ uv run facade.py
Storing cache data to file ./default.prefs
John
```

### Flyweight
The Flyweight design pattern is used when a system needs to handle a large number of similar objects. Instead of creating a new object for every instance, it reuses (shares) existing objects to reduce memory footprint and improve efficiency.

PROS:
* Reduces memory usage by sharing common state between objects
* Improves performance when handling many similar objects
* Decouples intrinsic (shared) state from extrinsic (unique) state

CONS:
* Increases code complexity (requires splitting state into intrinsic vs. extrinsic)
* May complicate object lifecycle management
* Can reduce clarity if overused


output of flyweight.py
```
$ uv run structural/flyweight/flyweight.py
S S P M S S S M S S S M S P P M P P P M M P S P M S S S M M S S S P P S P S P S M M P S M S S M S S M M M P M M P M M M M P P P M S M M P S S P P S P M M S P S P S P M S M P S P P P S P S S M S P M S P M P P S M M S P M S S P S S M S P M S P P S S S S S P P P S S P P S P P S P P S P M P P P M S M M P S P P S M M P M P M P S P S S M M S M M P S P S S S S P S P S M P M S P M S M P M P M M M P S M P M S P S M P P S M M M S M M M P S P S P M P M P P S M P P S S P P P S P M S S S M P P M P M P S M S M P M P P M P M P S M P S M S M M S M S M P S S P S P M S S P P S S S P M P S M P P S M P S M M S M M P M S M S P P S S P M M S M P M S M P P M S S S M P M S S S P S S S P S M M M M P S M M P S P S P S S S M M P M M P M P P S P P M P S P S S P M M P P M P P M P P P M P M S S S P M P S P P S M M P S M P S M M S P P S S M M M S P P M M P P M S M P S S M M P P M P P S M M P M S S S S P S S P S P S S P P S P M M P P P M P M P M P M S M S S S P S M P P P S S S S P M P S S S P M M S P M M M M P P M P %                                              
```

## Behavioural
Patterns that define how objects and classes interact and distribute responsibility
