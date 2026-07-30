# Python - Inheritance

This project covers inheritance in Python: base and derived classes,
multiple inheritance, method overriding, and the built-in functions
used to inspect relationships between objects and classes
(`isinstance`, `issubclass`, `type`, `super`).

## Learning Objectives
- What is a superclass, baseclass, or parentclass, and what is a
  subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another, and define multiple base
  classes
- What is the default class every class inherits from
- How to override an inherited method or attribute
- Which attributes or methods are available by heritage to
  subclasses
- What are, when, and how to use isinstance, issubclass, type, and
  super

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- All files start with `#!/usr/bin/python3`
- All files end with a new line
- All files are executable
- Code follows pycodestyle 2.7.*
- Every module, class, and method has a real docstring
- Test files live under `tests/` as `.txt` doctest files, run with
  `python3 -m doctest ./tests/*`

## Files
| File | Description |
|------|-------------|
| 0-lookup.py | List all attributes/methods of an object |
| 1-my_list.py | A list subclass with print_sorted() |
| 2-is_same_class.py | Check for an exact class match |
| 3-is_kind_of_class.py | Check for a class match or subclass |
| 4-inherits_from.py | Check for genuine inheritance |
| 5-base_geometry.py | An empty BaseGeometry class |
| 6-base_geometry.py | BaseGeometry with an unimplemented area() |
| 7-base_geometry.py | BaseGeometry with integer_validator() |
| 8-rectangle.py | Rectangle built on BaseGeometry |
| 9-rectangle.py | Rectangle with area() and __str__ |
| 10-square.py | Square built on Rectangle |
| 11-square.py | Square with its own __str__ |
| tests/1-my_list.txt | Doctest for MyList |
| tests/7-base_geometry.txt | Doctest for integer_validator |
