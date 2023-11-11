#!/usr/bin/python3
'''
Write a function that returns True if the object is exactly
an instance of the specified class; otherwise False.
'''

def is_same_class(obj, a_class):
    return isinstance(obj, a_class)

# Example usage:
class ExampleClass:
    pass

obj1 = ExampleClass()
obj2 = "This is a string"

print(is_same_class(obj1, ExampleClass))  # True
print(is_same_class(obj2, ExampleClass))  # False
