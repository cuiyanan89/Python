#!/usr/bin/python
#encoding:utf-8
import os
import stat
empty_file_names = []
empty_dir_names = []
file_names = []
    
def my_list(root):
    try:
        g = os.walk(root)
    except IOError , e:
        print '%s does not exist'%root
    r,d,f = g.next()
    if d == [] and f == []:
        empty_dir_names.append(r)
    for i in f:
        ff = os.path.join(r,i)
        if os.stat(ff).st_size == 0:
            empty_file_names.append(ff)
        file_names.append(ff)
    for j in d:
        rr = os.path.join(r,j)
        my_list(rr)
    
def qingli():
    for i in empty_file_names:
        os.remove(i)
        print '删除%s'%i
    for j in empty_dir_names:
        os.removedirs(j)
        print '删除%s'%j

def shadu():
    for name in file_names:
        f = open(name)
        s = f.read()
        if 'bad' in s:
            print 'has "bad"in contents delete %s'%name
            os.remove(name)
   
my_list(r'/csvt/n12/python_note/filetext/')
for name in file_names:
    print 'file>',name
for name in empty_dir_names:
    print 'emptydir>',name
for name in empty_file_names:
    print 'emptyfile>',name
shadu()
qingli()
