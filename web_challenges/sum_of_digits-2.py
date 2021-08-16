#!/usr/bin/env python3
def digit_sum(n):
    '''(int)->number
    Returns the sum of all the digits in the given integer, n'''
    if n<10:
        return n
    return n%10 + digit_sum(n//10)

def digital_root(n):
    '''(int)->number
    Returns the resulting sum of the digits in the given integer until it reaches a single digit number; via digit_sum'''
    while n>9:
        n=sum(digit_sum(n))
    return n

n=20
print(digital_root(n))

