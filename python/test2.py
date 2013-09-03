#!/usr/bin/python
#encoding=utf-8

def Abs_my(num):
    if type(num) == int or type(num) == float:
        if num < 0:
            return -num
        else:
            return num
def Max_my(l):
    if l.__len__():
        x = l[0]
        for i in l:
            if x < i:
                x = i
        return x

def Min_my(l) :      
    if l.__len__():
        x = l[0]
        for i in l:
            if x > i:
                x = i
        return x

if __name__ == '__main__':
    x = Abs_my(input('输入一个数字'))
    print '绝对值为%s'%x
    l = Max_my(input('输入列表'))
    print '最大值为%d'%l
    l = Min_my(input('输入列表'))
    print '最小值为%d'%l
