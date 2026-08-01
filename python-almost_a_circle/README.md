# Python - Almost a Circle

This project is a review of everything covered so far in Python:
imports, exceptions, classes, private attributes, getters/setters,
class and static methods, inheritance, unit testing, and file I/O —
plus new concepts: `*args`/`**kwargs`, and JSON serialization.

A `Base` class manages id generation and JSON (de)serialization for
every other class. `Rectangle` inherits from `Base`, and `Square`
inherits from `Rectangle`.

## Learning Objectives
- What unit testing is, and how to implement it in a large project
- How to serialize and deserialize a class
- How to write and read a JSON file
- What `*args` and `**kwargs` are, and how to use them
- How to handle named arguments in a function

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- All files start with `#!/usr/bin/python3`
- All files end with a new line and are executable
- Code follows pycodestyle 2.7.*
- Every module, class, and method has a real docstring
- Tests live under `tests/`, mirroring the project structure, and
  are run with `python3 -m unittest discover tests`

## Files
| File | Description |
|------|-------------|
| models/base.py | Base class: id management, JSON (de)serialization |
| models/rectangle.py | Rectangle class, built on Base |
| models/square.py | Square class, built on Rectangle |
| tests/test_models/test_base.py | Unit tests for Base |
| tests/test_models/test_rectangle.py | Unit tests for Rectangle |
| tests/test_models/test_square.py | Unit tests for Square |
