#!/bin/python3
#Check whether the input is integer
import sys

S = input().strip()
try: 
    print(int(S))
except:
     print('Bad String')
