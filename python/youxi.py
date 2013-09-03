#!/usr/bin/python
print "Welcome to the hero's world"
name =raw_input("Please input your name--->")
hero=[name,100]
print "Hero's name is %s and your Life is %d" % (hero[0],hero[1])
raw_input("input 'Enter' to go forward")
for i in range(3):
    hero[1]-=1
print "You stepped on a landmine,your Life down 3,your Life is %d" % hero[1]
raw_input("input 'Enter' to go forward")
hero.append('sword')
print 'you have a %s now ^_^' % hero[2]
raw_input("input 'Enter' to go forward")
del hero
print 'encounter the BOSS you die......= =|||'


