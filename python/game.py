#!/usr/bin/python
#encoding=utf-8
import random


def knife():
    if not hero.get('knife',False):
        print '你得到了一把刀'
        hero['knife']=1
    else:
        print '您升级了您的刀'
        hero['knife']+=1

def equip():
    if not hero.get('equip',False):
        print '你得到了盔甲'
        hero['equip']=1
    else:
        print '您升级了你的盔甲'
        hero['equip']+=1

def mine():
    if not hero.get('mine',False):
        print '你踩地雷了，掉15格血'
        hero['mine']=1
        hero['life']-=15
    else:
        print '你又踩雷了,再次降血15格'
        hero['mine']+=1
        hero['life']-=15

def bun():
    if not hero.get('bun',False):
        print '你捡到了包子，恭喜你加15格血'
        hero['bun']=1
        hero['life']+=15
    else:
        print '恭喜你又捡包子了，再次加血15格'
        hero['bun']+=1
        hero['life']+=15
def shuxing():
    print '-------------------------------------------------'
    print '英雄-----------生命值-----------%s'%hero['life']
    print 'BOSS-----------生命值-----------%s'%boss_life
    print '-------------------------------------------------'
def shuxing2():
    print '-------------------------------------------------'
    dian = ''
    dian2 = ''
    for i in range(hero['life']/10+1):
        dian+='*'
    for i in range(boss_life/10+1):
        dian2+='*'
    print '英雄:%s'%dian
    print 'BOSS:%s'%dian2
    print '-------------------------------------------------'
   
def yingxiong():
    print '-------------------------------------------------'
    print '姓名:%s 生命值:%d 武器:%s 盔甲:%s 地雷:%s 包子:%s'%(hero['name'],hero['life'],hero.get('knife','no knife'),hero.get('equip','no equip'),hero.get('mine','no mine'),hero.get('bun','no bun'))
    print '-------------------------------------------------'
choice = [knife,equip,bun,mine]
b = {'w':0,'s':1,'a':2,'d':3}
hero = {}
print '----------------欢迎来到游戏------------------'
print '----------------英雄进入城堡------------------'
hero['name'] = raw_input('---请输入您的姓名------------------->')
hero['life'] = 100
print '-------------------------------------------------'
print '|    您的英雄姓名为%s，初始生命值为%d'%(hero['name'],hero['life'])
print '|    在跟BOSS对决之前您有10步可以用于搜集装备'
print '-------------------------------------------------'

for i in range(10):
    random.shuffle(choice)
    yourchoice = raw_input('英雄你下一步打算怎么走(w前s后a左d右)-------->')
    if yourchoice not in 'awsd':
        print '请输入正确字符，你损失了一次机会'
        continue
    choice[b[yourchoice]]()
if hero['life'] <= 0:
    print '英雄被被雷炸死了= =|||'
yingxiong()
boss_life = 200
print "！！！！！BOSS来了,英雄注意！！！！！"
#shuxing()
shuxing2()
while hero['life'] >= 0:
    raw_input('英雄准备接招')
    hit = random.randint(20,40)
    if hit >= 35:
        print 'BOSS放出了一记大招,杀伤力%s'%hit
    else :
        print 'BOSS放出一普通招数,杀伤力%s'%hit

    if hero.get('equip',False):
        print '你的盔甲为你挡下了这一击，盔甲受损一次'
        hero['equip']-=1
    else :
        hero['life']-=hit
        if hero['life']<=0:
            print '英雄死掉了'
            hero['life']=0
            yingxiong()
            break
        print '你没有盔甲保护受到招数伤害，生命值降为%d'%hero['life']

    raw_input('英雄请回击')
    hit = random.randint(20,30)
    if hero.get('knife',0) > 0:
        for i in range(hero['knife']):
            hit += 10
        print '你的武器为你增加了攻击力,攻击力:%s,武器磨损一次'%hit
        hero['knife']-=1
        boss_life-=hit
    else:
        print '你徒手攻击BOSS，杀伤力%s对其造成伤害'%hit
        boss_life-=hit
    if boss_life <= 0:
        print 'BOSS被干掉，英雄胜利'
        yingxiong()
        break
#    shuxing()
    shuxing2()
