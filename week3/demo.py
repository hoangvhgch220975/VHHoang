#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'convert_weekday' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def convert_weekday(number):
    if number == 1:
        print('Sunday')
    elif number == 2:
        print('Monday')
    elif number == 3:
        print('Tuesday')
    elif number == 4:
        print('Wednesday')
    elif number == 5:
        print('Thursday')
    elif number == 6:
        print('Friday')
    elif number == 7:
        print('Saturday')
    else:
        print('Invalid value')
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # DO NOT CHANGE IN HERE

    n = int(input().strip())

    wd = convert_weekday(n)

    fptr.write(wd + '\n')

    fptr.close()
