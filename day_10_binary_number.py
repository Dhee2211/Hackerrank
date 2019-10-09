#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def binary(n):
    'Convert the number in binary and check consecutive 1 in the binary digit'
    max_value = 0
    count = 0
    while (n >0):
        rem = n%2
        n = n//2
        if rem == 1:
            count = count +1
        else:
            count = 0
        max_value = max(count, max_value)
    print(max_value)

#Run the following code
if __name__ == '__main__':
    n = int(input())
    binary(n)
