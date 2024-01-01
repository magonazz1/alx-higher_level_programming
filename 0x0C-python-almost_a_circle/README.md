# 0x0C. Python - Almost a Circle

![giphy.gif](./rcs/giphy.gif)

## Introduction
This project is a part of the Higher-level Python curriculum, focusing on various aspects of Python programming, including Object-Oriented Programming (OOP) principles. The goal is to prepare you for more advanced projects, such as the AirBnB project.

## Learning Objectives
After completing this project, you should be able to:

- Implement Unit testing in a large project
- Serialize and deserialize a class
- Read and write JSON files
- Understand and use *args and **kwargs in Python functions
- Handle named arguments in functions

## Project Structure
The project is divided into several tasks, each building upon the previous one. The tasks cover topics such as creating base classes, implementing inheritance, writing unit tests, and handling JSON serialization.

## Project Tasks
1. **If it's not tested, it doesn't work**
   - All files, classes, and methods must be unit tested and adhere to PEP 8 standards.

2. **Base class**
   - Create a base class with a private class attribute, constructor, and methods to manage the 'id' attribute.

3. **First Rectangle**
   - Write a class Rectangle that inherits from the base class.
   - Implement private instance attributes with getters and setters.

4. **Validate attributes**
   - Update the Rectangle class to add validation for attributes (width, height, x, y).

5. **Area first**
   - Add a method to calculate and return the area of a Rectangle instance.

6. **Display #0**
   - Implement a method to display a Rectangle instance using the '#' character.

7. **__str__**
   - Override the `__str__` method in the Rectangle class to represent the instance as a string.

8. **Display #1**
   - Improve the display method to consider the values of 'x' and 'y'.

9. **Update #0**
   - Add a method to update attributes using no-keyword arguments.

10. **Update #1**
    - Modify the update method to accept keyword arguments.

11. **And now, the Square!**
    - Write a class Square that inherits from the Rectangle class.

12. **Square size**
    - Add getters and setters for the 'size' attribute in the Square class.

13. **Square update**
    - Implement a method to update attributes in the Square class.

14. **Rectangle instance to dictionary representation**
    - Add a method to convert a Rectangle instance to a dictionary.

15. **Square instance to dictionary representation**
    - Add a method to convert a Square instance to a dictionary.

16. **JSON string to dictionary**
    - Implement a static method in the base class to convert a JSON string to a list of dictionaries.

17. **Dictionary to Instance**
    - Add a class method to create an instance from a dictionary.

18. **JSON string to file**
    - Implement a class method to save a list of instances to a JSON file.

## Requirements
- Python Scripts
  - Allowed editors: vi, vim, emacs
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - Your code should use the pycodestyle (version 2.8.*)
  - All your files must be executable
  - The length of your files will be tested using `wc`
  - All your modules should be documented using `python3 -c 'print(__import__("my_module").__doc__)'`
  - All your classes and functions should be documented
  - A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method.

- Python Unit Tests
  - Allowed editors: vi, vim, emacs
  - All your test files should be inside a folder named 'tests'
  - You have to use the unittest module
  - All your test files should be Python files (extension: .py)
  - All your test files and folders should start with 'test_'
  - Your file organization in the 'tests' folder should be the same as your project structure.
  - All your tests should be executed by using the command: `python3 -m unittest discover tests`

## Usage
To test the project, run the following command in the terminal:

```bash
python3 -m unittest discover tests
```

## Conclusion - Project 0x0C: Python - Almost a Circle

The **0x0C: Python - Almost a Circle** project is a comprehensive exploration of Python, focusing on Object-Oriented Programming (OOP) principles. The project provides a hands-on learning experience in various Python concepts, including:

- **Import**: Understanding how to import modules in Python.
- **Exceptions**: Handling exceptions in Python for error management.
- **Class**: Creating and using classes in Python for OOP.
- **Private Attribute**: Implementing private attributes within a class.
- **Getter/Setter**: Utilizing getter and setter methods for attribute access control.
- **Class Method**: Defining class methods in Python classes.
- **Static Method**: Implementing static methods within a class.
- **Inheritance**: Understanding and applying the concept of inheritance in Python.
- **Unittest**: Writing unit tests for Python code.
- **Read/Write File**: Reading from and writing to files in Python.
- **args and kwargs**: Exploring and utilizing variable-length argument lists.
- **Serialization/Deserialization**: Working with serialization and deserialization of objects.
- **JSON**: Handling JSON encoding and decoding in Python.

The project involves the creation of a base class called `Base`, followed by the implementation of a `Rectangle` class and a `Square` class that inherit from the base class. Throughout the tasks, students learn about unit testing, attribute validation, area calculation, display methods, and updating object attributes. The project emphasizes good coding practices, documentation, and adherence to PEP 8 style guidelines.

Additionally, the project covers essential aspects such as handling named arguments, preventing plagiarism, writing a README file, and using version control with Git and GitHub. Students gain practical experience in creating modular and well-documented code, along with writing and executing unit tests for code verification.

In conclusion, the **0x0C: Python - Almost a Circle** project provides a solid foundation for Python programming, OOP, and software development best practices. It equips learners with the skills needed to tackle more advanced projects and sets the stage for further exploration of the Python language and its capabilities.
