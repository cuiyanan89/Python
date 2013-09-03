#!/usr/bin/python
import random

x = random.randint(0,100)
'''
for i in range(6):
    y = int(raw_input('please input your number------>'))
    if y < x:
        print 'try a little bigger number'
    elif y > x:
        print 'try a little smailer number'
    else:
        print 'good!!!!'
        raw_input()
        break
print 'the number is %s'%x
'''
#y = int(raw_input('------->'))
#while y !=x:
#    if y < x:
#        print 'try a little bigger number'
#    else:
#        print 'try a little smailer number'
#    y = int (raw_input('------>'))
num = 0 
while num <6:
    y = int(raw_input('please input your number------>'))
    if y < x:
        print 'try a little bigger number'
    elif y > x:
        print 'try a little smailer number'
    else:
        print 'good!!!!'
        raw_input()
        break
    num +=1
else:
    print 'sorry you loss'
