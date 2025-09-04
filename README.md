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

### Proxy
A Proxy is a structural design pattern that provides a placeholder or surrogate object that controls access to another object.
It implements the same interface as the real object so that it can be used interchangeably by clients.

Key points:
* Controls access to the real object (lazy initialization, security checks, logging, caching, etc.)
* Manages the lifecycle of the real object (create on demand, destroy, reset, etc.)
* Clients don’t need to know whether they are talking to the proxy or the real object.

PROS
* Can add access control, caching, logging, or lazy loading transparently
* Protects the real object from unauthorized access or heavy load
* Makes system more flexible (different proxies for different needs: remote proxy, virtual proxy, protection proxy, etc.)
* Keeps the client code unchanged (since proxy has the same interface)

CONS
* Adds an extra layer of indirection (slight overhead)
* Can increase complexity if overused
* Must carefully ensure proxy and real subject remain consistent with the same interface

Difference with Similar Patterns:
* Facade → provides a simplified interface to a complex subsystem. It doesn’t mimic the real object’s interface.
* Decorator → extends or modifies behavior of an object without managing its lifecycle.
* Proxy → looks like the real object (same interface) but manages its access/lifecycle.

output of proxy.py
```
$ uv run proxy.py 
Proxy image: Displaying : test.jpg
From disk
Real image: Loading test.jpg
Real Image: Displaying test.jpg

Proxy image: Displaying : test.jpg
From Cache
Real Image: Displaying test.jpg
```

## Behavioural
Patterns that define how objects and classes interact and distribute responsibility


### Chain Of Responsibility
allows you to pass a request along a chain of handlers.
Each handler either processes the request or forwards it to the next handler in the chain

This helps decouple the sender of the request from the receiver since the sender does not need to know which handler will take care of it

PROS
* Loose coupling between sender and receiver.
* Easy to add or remove handlers without modifying the client code.
* Increases flexibility in assigning responsibilities to different handlers.
* Makes code open for extension (add new handlers) but closed for modification (don’t touch existing ones).

CONS
* Debugging can be hard: not always clear which handler will process a request.
* If no handler processes the request, it might get lost silently.
* Performance overhead if the chain is long (request travels through many handlers).

Use Cases
* Event handling systems (UI frameworks where events are passed from child → parent)
* Middleware pipelines (e.g., Django/Express middlewares, logging chains)
* Customer support systems (L1 → L2 → Manager)
* Request validation pipelines

output of chain_of_responsibility.py:
```
$ uv run chain_of_responsibility.py
Header with authentication
Authorization: 123456
ContentType: json
Body: {"Username":"John"}

Header without authentication
ContentType: json
```

### Command
A Command pattern turns a request into a standalone object containing all information about the request.
This object can then be passed, queued, logged, or assigned to different handlers without knowing who or how it will be executed

Use Cases
* The invoker only knows it should call execute() on a command
* The receiver is the actual object that knows how to perform the action
* The command object sits in between and fully decouples sender from receiver
* Useful for Undo/Redo, task scheduling, logging, and macro recording

PROS
* Decouples sender (client) from receiver (executor)
* Requests can be queued, logged, undone, or redone easily
* Supports ordering, scheduling, and prioritization
* Improves flexibility when adding new commands

CONS
* Increases number of classes (command per action)
* May add complexity for simple actions

output command.py:
```
$ uv run command.py 
Adding order with id: 1
Adding order with id: 2
Paying for order with id : 1
Paying for order with id : 2
```

### Interpreter
Interpreter Design Pattern

Interprets a language or expression based on a defined grammar.
Useful for parsing, evaluating expressions, and building small domain-specific languages (DSLs).
Can be implemented recursively to evaluate nested expressions

Components:
* Terminal Expression – the simplest, indivisible elements of the grammar (e.g., numbers, keywords)

* Non-Terminal Expression – composed of one or more Terminal or Non-Terminal expressions; typically evaluated recursively (e.g., addition, subtraction, conditional statements)

PROS:
* Simplifies the design of complex parsing logic
* Makes it easy to extend the language by adding new expressions
* Provides a clear separation between grammar and evaluation logic

CONS:
* Can become inefficient for large grammars or deep recursive structures
* Hard to maintain if the grammar is complex
* May require significant memory and stack space for recursion
* Not suitable for general-purpose programming languages with large syntax

Usage Examples:
* Simple expression evaluators (math calculators)
* nterpreting configuration files or DSL scripts
* Building rule engines

output of interpreter.py:
```
$ uv run interpreter.py
19.4
```

### Iterator
Provides a way to access the elements of a collection sequentially without exposing its underlying representation

Key points:
* Traverse a collection (array, list, tree, etc.)
* Implements two main methods:
* has_next() – checks if there are more elements to iterate over
* next() – returns the next element in the sequence

Use Cases:
* When you want to iterate over a collection but hide its internal structure
* When you need multiple ways of iterating over the same collection

PROS:
* Decouples collection from traversal logic
* Multiple iterators can coexist for the same collection
* Simplifies client code

CONS:
* Adds extra classes/interfaces for iteration
* Slight overhead if used for very simple or small collections

output of iterator.py:
```
$ uv run iterator.py
Alex
Carol
John
Michael
Michael
John
Carol
Alex
```
