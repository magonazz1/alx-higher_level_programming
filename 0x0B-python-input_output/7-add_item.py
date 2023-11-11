#!/usr/bin/python3

from sys import argv
from os.path import exists
from json import dump, load

# Importing functions directly
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

"""
Write a script that adds all
arguments to a Python list, and then
save them to a file
"""

filename = 'add_item.json'

# Check if the file exists
my_list = load_from_json_file(filename) if exists(filename) else []

# Append command-line arguments to the list
my_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

