# Project Overview

The 0x05. Python - Exceptions project introduces you to the world of Python error handling and exceptions. In programming, exceptions are events that can disrupt the normal flow of code execution. This project aims to teach you how to handle these exceptions and errors effectively.

## Project Details

**Author**: Martin Magonagona
**Email**: martinmagonazz@outlook.com

## Objectives

By the end of this project, you will be able to explain to anyone, without the help of Google:

- Why Python programming is awesome.
- The difference between errors and exceptions.
- What exceptions are and how to use them.
- When to use exceptions.
- How to correctly handle exceptions.
- The purpose of catching exceptions.
- How to raise a built-in exception.
- When to implement a clean-up action after an exception.

Now, let's break down each task within this project.

## Task 0: Safe List Printing

In this task, you need to write a Python function that prints a specified number of elements from a given list. You should handle exceptions gracefully, even if the number of elements to print is greater than the length of the list.

**Prototype:** `def safe_print_list(my_list=[], x=0)`

## Task 1: Safe Printing of an Integers List

This task requires you to write a Python function that prints an integer using the `"{:d}".format()` method. You should check if the value is an integer and return `True` if it's printed successfully; otherwise, return `False`.

**Prototype:** `def safe_print_integer(value)`

## Task 2: Print and Count Integers

In this task, you are tasked with writing a Python function that prints the first x elements of a list, focusing only on integers. You should handle exceptions and skip any non-integer values in silence.

**Prototype:** `def safe_print_list_integers(my_list=[], x=0)`

## Task 3: Integers Division with Debug

Your job in this task is to create a Python function that divides two integers and prints the result. You should also handle exceptions and print "Inside result" before displaying the division result or "None" if an exception occurs.

**Prototype:** `def safe_print_division(a, b)`

## Task 4: Divide a List

In this task, you need to write a Python function that divides elements in two lists element by element. The function should return a new list with all divisions, ensuring that the division by zero results in 0. You must also handle any invalid elements and print the appropriate error messages.

**Prototype:** `def list_division(my_list_1, my_list_2, list_length)`

## Task 5: Raise Exception

For this task, you need to create a Python function that raises a type exception.

**Prototype:** `def raise_exception()`

## Task 6: Raise a Message

In this task, you are required to write a Python function that raises a name exception with an optional message.

**Prototype:** `def raise_exception_msg(message="")`

## Task 7: Safe Integer Print with Error Message (Advanced)

This advanced task involves creating a Python function that prints an integer with error handling. The function should return `True` if the value is printed successfully or `False` if an error occurs. If an error occurs, an error message should be printed to stderr.

**Prototype:** `def safe_print_integer_err(value)`

## Task 8: Safe Function (Advanced)

In this advanced task, you need to create a Python function that safely executes another function. The function should return the result of the executed function or `None` if something goes wrong. Additionally, if an error occurs, an error message should be printed to stderr.

**Prototype:** `def safe_function(fct, *args)`

## Task 9: ByteCode -> Python #4 (Advanced)

In this advanced task, you are asked to write a Python function that does exactly the same as a provided Python bytecode.

**Prototype:** `def magic_calculation(a, b)`

## Task 10: CPython #2: PyFloatObject (Advanced)

This advanced task requires creating three C functions that print basic information about Python lists, Python bytes, and Python float objects. These functions need to handle invalid objects gracefully.

## Usage and Testing

Each task is implemented as a separate Python script that can be executed independently. Simply run the scripts to test each task.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**Happy coding!**
