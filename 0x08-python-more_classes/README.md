# Project Description: Python - More Classes and Objects

## Introduction
Welcome to the Python - More Classes and Objects project! In this project, you will dive deeper into Object-Oriented Programming (OOP) with Python. You will explore concepts related to classes, objects, attributes, methods, and more. The project consists of several tasks, each designed to enhance your understanding of Python's OOP capabilities.

## Learning Objectives
By the end of this project, you should be able to explain the following topics without needing external resources:

- Why Python programming is awesome
- What is Object-Oriented Programming (OOP)
- The concept of "first-class everything"
- What is a class and what is an object (or instance)
- The difference between a class and an object or instance
- What is an attribute and how to use public, protected, and private attributes
- The role of `self` in Python classes
- What is a method in Python
- Understanding the special `__init__` method and how to use it
- Concepts of Data Abstraction, Data Encapsulation, and Information Hiding
- The concept of a property
- The difference between an attribute and a property in Python
- Pythonic ways to write getters and setters
- The special `__str__` and `__repr__` methods and how to use them
- Differentiating between `__str__` and `__repr__`
- Understanding class attributes and their differences from object attributes
- Class methods and static methods
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- The role of `__dict__` in a class and instance
- How Python finds the attributes of an object or class
- How to use the `getattr` function

## Requirements
- You are allowed to use the following text editors: `vi`, `vim`, `emacs`
- All your Python files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Ensure all your Python files end with a newline character
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of your project folder is mandatory
- Your code should follow the PEP 8 style guide (use `pycodestyle` version 2.8.*)
- All your Python files must be executable
- The length of your Python files will be tested using `wc`

## Task Summaries
Here is an overview of the tasks you'll be working on:

### Task 0: Simple Rectangle
Create an empty class `Rectangle` that defines a rectangle.

### Task 1: Real Definition of a Rectangle
Enhance the `Rectangle` class by adding private instance attributes, properties, and an `__init__` method to set width and height.

### Task 2: Area and Perimeter
Extend the `Rectangle` class to include methods for calculating area and perimeter of the rectangle.

### Task 3: String Representation
Enhance the `Rectangle` class to provide a string representation of the rectangle using `__str__` and `__repr__` methods.

### Task 4: Eval is Magic
Modify the `Rectangle` class to enable the creation of new instances from a string representation.

### Task 5: Detect Instance Deletion
Implement a mechanism in the `Rectangle` class to print a message when an instance of `Rectangle` is deleted.

### Task 6: How Many Instances
Add a class attribute `number_of_instances` to track the number of `Rectangle` instances created and deleted.

### Task 7: Change Representation
Extend the `Rectangle` class to include a public class attribute for specifying the symbol used in string representation.

### Task 8: Compare Rectangles
Implement a static method `bigger_or_equal` to compare two rectangles based on their areas.

### Task 9: A Square is a Rectangle
Add a class method `square` to create a new instance of `Rectangle` where the width and height are equal.

### Task 10: N Queens (Advanced)
Solve the N Queens puzzle, which involves placing N non-attacking queens on an N×N chessboard. The program should print every possible solution to the problem.

## Getting Started
1. Clone the project repository: [alx-higher_level_programming](https://github.com/USERNAME/alx-higher_level_programming)
2. Navigate to the project directory: `0x08-python-more_classes`
3. Start working on the tasks, one by one, and implement the required code in Python.

Have fun exploring and expanding your knowledge of Python's Object-Oriented Programming concepts in this project! If you have any questions or need assistance, feel free to reach out to the project mentor or your peers. Happy coding!
