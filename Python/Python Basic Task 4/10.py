#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    list = s.split(" ")
    capitalize_list = []
    for i in list:
        capitalize_list.append(i.capitalize())
    new_string = " ".join(capitalize_list)   
    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
