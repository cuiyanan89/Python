#!/usr/bin/python

class fangzi():
    gongyou = 'gouyoushuxing'
    __siyou = 'siyoushuxing'

    def __init__(self,name):
        self.name = name
        print self.name
    
    def leifangfa(cls):
        print 'leifangfa'
    def __siyoufangfa():
        print '__siyoufangfa'
    @classmethod
    def gongyou_zhuan_leifangfa(cls):
        print gongyou
    def xianshisiyoushuxing():
        print __siyou
