#!/usr/bin/python
#encoding=utf-8
import os,time,random

l = '*'*61
ll = '\n*'+' '*59+'*'
map_str = l+ll*25+'\n'+l
os.system('/usr/bin/clear')
#print map_str
#time.sleep(2)
#os.system('/usr/bin/clear')
map_list = list(map_str)
#map_list[80]='*'
#map_str = ''
#for i in map_list:
#    map_str += i
#print map_str


def map_fenge(height_up,height_down,width_left,width_right):
    if height_down - height_up == 2 or width_right - width_left ==2:
        return
#一个方向达到最窄后不再分割
    global map_list
    x = random.choice(xrange(height_up+2,height_down,2))
#x为横向分割线
    y = random.choice(xrange(width_left+2,width_right,4))
#y为纵向分割线
    for i in xrange(1,60):
        map_list[x*62+i]='*'
    for j in xrange(1,26):
        map_list[y+j*62]='*'
    open_list = [0,1,1,1]
    random.shuffle(open_list)
    open_choice_list = []
    
#    open_choice_list.append(random.choice(xrange(width_left+1,y-1,2)))
#    open_choice_list.append(random.choice(xrange(height_up+1,x-1,2)))
#    open_choice_list.append(random.choice(xrange(y+1,width_right-1,2)))
#    open_choice_list.append(random.choice(xrange(x+1,height_down-1,2)))
    if open_list[0]==1:
#        map_list[x*62+open_choice_list[0]] ='@'
        map_list[x*62+random.choice(xrange(width_left+1,y,2))]=' '
    if open_list[1]==1:
#        map_list[y+open_choice_list[1]*62] ='@'
        map_list[y+random.choice(xrange(height_up+1,x,2))*62] =' '
    if open_list[2]==1:
#        map_list[x*62+open_choice_list[2]] ='@'
        map_list[x*62+random.choice(xrange(y+1,width_right,2))] =' '
    if open_list[3]==1:
#        map_list[y+open_choice_list[3]*62] ='@'
        map_list[y+random.choice(xrange(x+1,height_down,2))*62] =' '
map_fenge(0,26,0,60)
os.system('/usr/bin/clear')
map_str = ''
for i in map_list:
    map_str += i
print map_str
