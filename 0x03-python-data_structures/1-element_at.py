#!/usr/bin/python3

def element_at(my_list, idx):

    n_mylist = len(my_list)

    if (idx < 0):
        return(NONE)

    elif (idx > (n_mylist) - 1):
        return(NONE)

    else:
        return(my_list[idx])
