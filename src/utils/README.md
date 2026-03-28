"""
Core Engine
================

A high-performance, scalable, and maintainable software engine for complex applications.

Installation
------------

To install the core engine, run the following command:

    pip install core-engine

Usage
-----

The core engine provides a set of APIs for building and managing complex systems.

### Example Usage

```python
from core_engine import Engine

# Create a new engine instance
engine = Engine()

# Add a component to the engine
engine.add_component("my_component")

# Start the engine
engine.start()
```

API Documentation
--------------

The core engine provides the following APIs:

### Engine

* `add_component(name: str)`: Adds a new component to the engine.
* `start()`: Starts the engine.
* `stop()`: Stops the engine.

### Component

* `__init__(self, name: str)`: Initializes a new component instance.
* `start()`: Starts the component.
* `stop()`: Stops the component.
"""

class Engine:
    def __init__(self):
        self.components = {}

    def add_component(self, name: str):
        if name in self.components:
            raise ValueError(f"Component '{name}' already exists.")
        self.components[name] = Component(name)

    def start(self):
        for component in self.components.values():
            component.start()

    def stop(self):
        for component in self.components.values():
            component.stop()

class Component:
    def __init__(self, name: str):
        self.name = name
        self.running = False

    def start(self):
        self.running = True
        print(f"Component '{self.name}' started.")

    def stop(self):
        self.running = False
        print(f"Component '{self.name}' stopped.")