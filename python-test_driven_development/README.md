# Python - Test-driven development

This project practices Test-Driven Development (TDD) in Python:
writing docstring-based interactive tests (doctests) and real
`unittest` tests, and thinking through edge cases before (and while)
writing the implementation.

## Learning Objectives
- What's an interactive test, and why tests are important
- How to write docstrings to create tests
- How to write documentation for each module and function
- The basic option flags used to run tests
- How to find edge cases

## Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- All files start with `#!/usr/bin/python3`
- All files end with a new line and are executable
- Code follows pycodestyle 2.7.*
- Every module and function has a real docstring
- Doctest files live under `tests/` as `.txt` files, run with
  `python3 -m doctest ./tests/*`
- Task 6 additionally has a real `unittest` file, run with
  `python3 -m unittest tests.6-max_integer_test`

## Files
| File | Description |
|------|-------------|
| 0-add_integer.py | Add two integers, casting floats first |
| tests/0-add_integer.txt | Doctest for add_integer |
| 2-matrix_divided.py | Divide every element of a matrix |
| tests/2-matrix_divided.txt | Doctest for matrix_divided |
| 3-say_my_name.py | Print "My name is ..." |
| tests/3-say_my_name.txt | Doctest for say_my_name |
| 4-print_square.py | Print a square made of # |
| tests/4-print_square.txt | Doctest for print_square |
| 5-text_indentation.py | Print text with extra newlines |
| tests/5-text_indentation.txt | Doctest for text_indentation |
| 6-max_integer.py | Find the max integer in a list |
| tests/6-max_integer_test.py | Unittest for max_integer |
