#!/usr/bin/python
import re

def count():
    hello_re = re.compile(r'\bhello\b')
    f = open('hello.txt')
    s = f.read()
    hello_list = hello_re.findall(s)
    f.close()
    print hello_list.__len__()


def sub_hello():
    f = open('hello.txt','r+')
    s = f.read()
    print s 
    f.truncate()
    f.flush()
    f.seek(0,0)
    s = re.sub(r'hello',r'good',s)
    print s
    f.write(s)
    f.close()

def write_again():
    f= open('hello.txt','r')
    s = f.read()
    f.close()
    s = re.sub(r'hello',r'good',s)
    f = open('hello.txt','w')
    f.write(s)
    f.close()
count()
sub_hello()
#write_again()
