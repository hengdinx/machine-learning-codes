#!/usr/bin/python

def is_ss(x):
    for i in range(2,x/2+1):
        if x % i == 0:
            return False
    return True
a=is_ss(7)
print a
print filter(is_ss,range(1,101))
