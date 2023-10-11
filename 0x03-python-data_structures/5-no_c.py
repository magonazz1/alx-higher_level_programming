#!/usr/bin/python3

def no_c(my_string):

    rem = ""

    for chr in my_string:
        if ((chr != 'c') and (chr != 'C')):
            rem = rem + chr
    return (rem)
