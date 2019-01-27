#!/bin/python

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(arr):
    prevVal = count = 1
    history = 0
    prev = arr[0]
    for i in arr[1:]:
        if i < prev:
            count += 1
            if prevVal == 1:
                history += 1
            prevVal = 1
        elif i == prev:
            count += 1
            prevVal = 1
            count += (history * (history+1))/2
            history = 0
        else:
            count += (prevVal + 1)
            prevVal = prevVal + 1
            count += (history * (history+1))/2
            history = 0
        prev = i
        # print i, count
    count += (history * (history+1))/2
    return count

if __name__ == '__main__':
    numList = map(int, raw_input().split())
    print candies(numList)
