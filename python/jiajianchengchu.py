#!/usr/bin/python

def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return float(x)/y
def yu(x,y):
    return x%y

fiction = {'+':jia,'-':jian,'*':cheng,'/':chu,'%':yu}

put_in = raw_input()
while put_in != 'q':
    for i in put_in:
        if i in '+-*/%':
            x,y=put_in.split(i)
            if '.' in x or '.' in y:
                x = float(x)
                y = float(y)
            else:
                x = int(x)
                y = int(y)
            print fiction[i](x,y)
    put_in = raw_input()
