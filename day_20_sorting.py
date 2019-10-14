#!/bin/python3

import sys
number_of_swaps = 0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bublesort(a):
    number_of_swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                number_of_swaps = number_of_swaps + 1
        if number_of_swaps == 0:
            break
    return number_of_swaps
number = bublesort(a)
print(f'Array is sorted in { number } swaps.')
print(f'First Element: { a[0] }')
print(f'Last Element: {a[len(a)-1]}')      
    