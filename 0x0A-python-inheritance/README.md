# Python Inheritance

Python Inheritance project for ALX Software Engineering program.

## Table of Contents
- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Files](#files)
- [Usage](#usage)

## Description

This project is a part of the ALX Software Engineering program and focuses on the concept of inheritance in Python. Inheritance is a fundamental feature of object-oriented programming (OOP) that allows one class to inherit attributes and methods from another class. This project helps you understand the principles of inheritance, how to create and use classes, and perform various tasks related to Python's OOP features.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the concept of inheritance in Python.
- Differentiate between a superclass, base class, and subclass.
- List attributes and methods of a class or instance.
- Understand how to inherit a class from another.
- Implement classes with multiple base classes.
- Recognize the default class from which all classes inherit.
- Override methods or attributes inherited from the base class.
- Understand how attributes and methods are available to subclasses by inheritance.
- Know the purpose of inheritance in Python.
- Use the `isinstance`, `issubclass`, `type`, and `super` built-in functions effectively.

## Requirements

### Python Scripts

- You are allowed to use the following editors: `vi`, `vim`, and `emacs`.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow the `pycodestyle` style guide (version 2.8.*).
- All your files must be executable.
- The length of your files will be tested using the `wc` command.

### Python Test Cases

- All your test files should be inside a folder named `tests`.
- All your test files should have a `.txt` extension.
- All your tests should be executed using the command: `python3 -m doctest ./tests/*`.
- All your modules should have documentation.
- All your classes should have documentation.
- All functions (inside and outside a class) should have documentation. A documentation is not just a word; it's a real sentence explaining the purpose of the module, class, or method.

## Tasks

The project consists of several tasks, each focusing on a specific aspect of Python inheritance. Here's a brief overview of the tasks:

1. `0-lookup.py`: Write a function that returns the list of available attributes and methods of an object.
2. `1-my_list.py`: Write a class `MyList` that inherits from the `list` class and provides a method to print the list in sorted order.
3. `2-is_same_class.py`: Write a function to check if an object is exactly an instance of the specified class.
4. `3-is_kind_of_class.py`: Write a function to check if an object is an instance of, or inherits from, a specified class.
5. `4-inherits_from.py`: Write a function to check if an object is an instance of a class that inherited from a specified class.
6. `5-base_geometry.py`: Define an empty class `BaseGeometry`.
7. `6-base_geometry.py`: Improve the `BaseGeometry` class by adding an `area()` method.
8. `7-base_geometry.py`: Add an `integer_validator()` method to the `BaseGeometry` class for integer validation.
9. `8-rectangle.py`: Create a `Rectangle` class that inherits from `BaseGeometry` and represents a rectangle.
10. `9-rectangle.py`: Enhance the `Rectangle` class to provide a more detailed description in `__str__` method.
11. `10-square.py`: Create a `Square` class that inherits from `Rectangle` and represents a square.
12. `11-square.py`: Improve the `Square` class by providing a more detailed description in `__str__` method.
13. `100-my_int.py`: Create a class `MyInt` that inherits from `int` and swaps the behavior of the equality operators `==` and `!=`.
14. `101-add_attribute.py`: Write a function to add an attribute to an object if possible.

## Files

The project consists of the following main files:

- `0-lookup.py`
- `1-my_list.py`
- `2-is_same_class.py`
- `3-is_kind_of_class.py`
- `4-inherits_from.py`
- `5-base_geometry.py`
- `6-base_geometry.py`
- `7-base_geometry.py`
- `8-rectangle.py`
- `9-rectangle.py`
- `10-square.py`
- `11-square.py`
- `100-my_int.py`
- `101-add_attribute.py`

Additionally, there are test files in the `tests` directory corresponding to each task.

## Usage

To run the Python scripts, simply execute them with a Python interpreter:

```bash
python3 script_name.py
```

For example, to run the script for Task 1:

```bash
python3 1-my_list.py
```

To run the tests, use the following command in the project directory:

```bash
python3 -m doctest ./tests/*
```
