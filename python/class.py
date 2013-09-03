#!/usr/bin/python
#encoding=utf-8
class Dog():
    mingzi = '豆豆'
    maose = '黄色'
    nianling = 10
    xingbie = '公'
    tui = 4
    pingzhong = '松狮'
    __siyou = 'kanbudao'

    def say(self):
        self.tmp = 'hello'
        print self.tmp
        print '姓名:%s,年龄:%d'%(self.mingzi,self.nianling)
    def run(self):
        print '用%d条腿跑'%self.tui

    def dayinsiyou(self):
        print '私有属性%s'%__siyou
print Dog().__dict__
gou = Dog()
gou.say()
gou.run()
print gou.mingzi
#gou.__siyou
print gou.__dict__
