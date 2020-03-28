import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    res = [0] * len(a)
    for i in range(len(a)):
        new_index = (i+(n-d)) % len(a)
        res[new_index] = a[i]
    return res

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(result)
