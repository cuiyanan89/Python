#!/usr/bin/python
def tihuan(str_0,str_1,str_2):
    if str_1 in str_0:
        return str_0[0:str_0.find(str_1)]+str_2+str_0[str_0.find(str_1)+len(str_1):]

print tihuan('Hello world','Hello','Good')
