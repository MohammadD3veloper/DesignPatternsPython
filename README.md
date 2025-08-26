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

## Structural
Patterns that focus on how classes and objects are composed to form larger structures, improving flexibility, testability, and scalability

## Behavioural
Patterns that define how objects and classes interact and distribute responsibility
