#!/usr/bin/python
def fib(n):
    a,b=0,1
    while b<n:
        print b
        a,b = b,a+b

def fib2(n):
    a,b = 0,1
    l = []
    while b<n:
        l.append(b)
        a,b = b,a+b
    return l
