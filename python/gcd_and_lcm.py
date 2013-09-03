#!/usr/bin/python
def gcd(num1,num2):
    print 'num1:%s,num2:%s'%(num1,num2)
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)

def lcm(num1,num2):
    tmp = gcd(num1,num2)
    return num1*num2/tmp
print  gcd(3,15)
