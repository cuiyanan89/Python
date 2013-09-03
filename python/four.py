#!/usr/bin/python
from __future__ import division
import sys
running = True
while running:
    try:
        t = raw_input()
        p = raw_input()
        if t.isdigit() and p.isdigit():
            t = int(t)
            p = int(p)
        else:
            print 'your input is not all digit,try again'
            continue
    except EOFError:
        break
    print 'operator + result\n',t+p
    print 'operator - result\n',t-p
    print 'operator * result\n',t*p
    print 'operator / result\n',t/p

