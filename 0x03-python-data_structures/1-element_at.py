#!/usr/bin/python3

def element_at(my_list, idx):

    n_mylist = (len(my_list) - 1)

    if (idx < 0) or (idx > n_mylist):
        return (NONE)

    return(my_list[idx])
