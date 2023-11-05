# Project Title

0x07. Python - Test-driven development

## Project Description

This project focuses on Test-Driven Development (TDD) using Python. The tasks involve writing Python functions while following TDD principles. For each task, you need to create the function and corresponding test cases using the doctest module. You must also write appropriate documentation and ensure your code follows the specified requirements.

The project is structured into several tasks, each with its own set of requirements. Below is a summary of each task:

### 0. Integers addition

Write a function that adds two integers.

- Function prototype: `def add_integer(a, b=98):`
- Input parameters `a` and `b` must be integers or floats; otherwise, raise a `TypeError` exception.
- If `a` or `b` are floats, they must be first casted to integers.
- The function returns an integer, which is the addition of `a` and `b`.
- You are not allowed to import any modules.

### 1. Divide a matrix

Write a function that divides all elements of a matrix.

- Function prototype: `def matrix_divided(matrix, div):`
- The input parameter `matrix` must be a list of lists of integers or floats; otherwise, raise a `TypeError` exception.
- Each row of the matrix must have the same size; otherwise, raise a `TypeError` exception.
- The input parameter `div` must be a number (integer or float); otherwise, raise a `TypeError` exception.
- If `div` is equal to 0, raise a `ZeroDivisionError` exception.
- Divide all elements of the matrix by `div`, rounded to 2 decimal places.
- Return a new matrix.
- You are not allowed to import any modules.

### 2. Say my name

Write a function that prints "My name is \<first name> \<last name>."

- Function prototype: `def say_my_name(first_name, last_name=""):`
- Both `first_name` and `last_name` must be strings; otherwise, raise a `TypeError` exception.
- You are not allowed to import any modules.

### 3. Print square

Write a function that prints a square with the character `#`.

- Function prototype: `def print_square(size):`
- The input parameter `size` is the size length of the square.
- `size` must be an integer; otherwise, raise a `TypeError` exception.
- If `size` is less than 0, raise a `ValueError` exception.
- You are not allowed to import any modules.

### 4. Text indentation

Write a function that prints a text with 2 new lines after each of these characters: `.` , `?` , and `:`.

- Function prototype: `def text_indentation(text):`
- The input parameter `text` must be a string; otherwise, raise a `TypeError` exception.
- Ensure there are no spaces at the beginning or end of each printed line.
- You are not allowed to import any modules.

### 5. Max integer - Unittest

Write unit tests for the `max_integer` function.

- Create a test file inside the `tests` directory.
- Use the `unittest` module for writing test cases.
- The test file should be executed using the command: `python3 -m unittest tests.6-max_integer_test`
- All tests should pass.

### 6. Matrix multiplication

Write a function that multiplies two matrices.

- Function prototype: `def matrix_mul(m_a, m_b):`
- Ensure that `m_a` and `m_b` are validated according to specified requirements.
- You are not allowed to import any modules.
- Test cases must cover various scenarios.

### 7. Lazy matrix multiplication

Write a function that multiplies two matrices using the NumPy module.

- Prototype: `def lazy_matrix_mul(m_a, m_b):`
- Ensure that `m_a` and `m_b` are validated according to the same requirements as in task 6.
- You are allowed to use the NumPy module.
- Test cases should be similar to task 6, but with new exception types/messages.

### 8. CPython #3: Python Strings (Advanced)

Create a CPython shared library function that prints Python strings.

- Prototype: `void print_python_string(PyObject *p);`
- Check if the given object is a valid string, and print its information.
- Print an error message if the object is not a valid string.

## Getting Started

Follow the instructions for each task and ensure you write appropriate documentation, create test cases, and meet the specified requirements. Use the provided sample code and test files as a reference.

## Prerequisites

- Python 3.4
- NumPy (for task 7)
- GCC compiler (for task 8)

## Authors

- Guillaume (provided the project)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
