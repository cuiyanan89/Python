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
    if height_down - height_up <= 2 or width_right - width_left <=2:
        return
#一个方向达到最窄后不再分割
    global map_list
    x = random.choice(xrange(height_up+2,height_down,2))
#x为横向分割线
    y = random.choice(xrange(width_left+2,width_right,2))
#y为纵向分割线
    for i in xrange(width_left+1,width_right-width_left):
#        print x,height_up,i,width_left
        map_list[(x+height_up)*62+i+width_left]='*'
    for j in xrange(width_left+1,height_down-height_up):
        map_list[y+(j+height_up)*62+width_left]='*'
    print 'x',x,'y',y,'up',height_up,'down',height_down,'left',width_left,'right',width_right,'i',i,'j',j,
    open_list = [0,1,1,1]
    random.shuffle(open_list)
    open_choice_list = []
    
    raw_input() 
    os.system('/usr/bin/clear')
    map_str = ''
    for i in map_list:
        map_str += i
    print map_str
#    open_choice_list.append(random.choice(xrange(width_left+1,y-1,2)))
#    open_choice_list.append(random.choice(xrange(height_up+1,x-1,2)))
#    open_choice_list.append(random.choice(xrange(y+1,width_right-1,2)))
#    open_choice_list.append(random.choice(xrange(x+1,height_down-1,2)))
    if open_list[0]==1:
        if width_left >=y-2:
            number = width_left+1
        else:
            number = random.choice(xrange(width_left+1,y,2))
#        map_list[x*62+open_choice_list[0]] ='@'
#        print 'y:',y,'number:',number,
        map_list[(x+height_up)*62+width_left+number]='1'
    if open_list[1]==1:
        if height_up>= x-2:
            number = height_up+1
        else:
            number = random.choice(xrange(height_up+1,x,2))
#        map_list[y+open_choice_list[1]*62] ='@'
#        print 'x:',x,'number:',number,
        map_list[y+(number+height_up)*62+width_left] ='2'
    if open_list[2]==1:
        if y >= width_right-2:
            number = y+1
        else:
            number = random.choice(xrange(y+1,width_right,2))
#        map_list[x*62+open_choice_list[2]] ='@'
#        print 'y:',y,'number:',number,
        map_list[(x+height_up)*62+width_left+number] ='3'
    if open_list[3]==1:
        if x >= height_down-2:
            number = x+1
        else:
            number = random.choice(xrange(x+1,height_down,2))
#        map_list[y+open_choice_list[3]*62] ='@'
#        print 'x:',x,'number:',number,
        map_list[y+(number+height_up)*62+width_left] ='4'
#    for i in range(4):
#        print open_list[i],
    raw_input() 
    os.system('/usr/bin/clear')
    map_str = ''
    for i in map_list:
        map_str += i
    print map_str
    map_fenge(height_up,x,width_left,y)
    map_fenge(x,height_down,width_left,y)
    map_fenge(x,height_down,y,width_right)
    map_fenge(height_up,x,y,width_right)
map_fenge(0,26,0,60)
