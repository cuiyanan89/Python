#!/usr/bin/python
#encoding=utf-8
import os,time,random
import getch

l = '#'*61
ll = '\n#'+' '*59+'#'
map_str = l+ll*25+'\n'+l
os.system('/usr/bin/clear')
map_list = list(map_str)
user = {'icon':'\x1b[1;41m\x1b[1;33m%s\x1b[0m','name':'Cuiyanan','life':100,'site':63}
def map_flush():
    global map_list
    map_str = ''
    os.system('/usr/bin/clear')
    for i in map_list:
        map_str += i
    print map_str
#    刷新地图

def map_fenge(height_up,height_down,width_left,width_right):
    if height_down - height_up <= 2 or width_right - width_left <=2:
        return
#一个方向达到最窄后不再分割
    global map_list
    x = random.choice(xrange(height_up+2,height_down,2))
#x为横向分割线
    y = random.choice(xrange(width_left+2,width_right,2))
#y为纵向分割线
    for i in xrange(1,width_right-width_left):
        map_list[(x)*62+i+width_left]='#'
    for j in xrange(1,height_down-height_up):
        map_list[y+(j+height_up)*62]='#'
    open_list = [0,1,1,1]
    random.shuffle(open_list)
    open_choice_list = []
    map_flush()    
#    os.system('/usr/bin/clear')
#    map_str = ''
#    for i in map_list:
#        map_str += i
#    print map_str
    if open_list[0]==1:
        if width_left >=y-2:
            number = width_left+1
        else:
            number = random.choice(xrange(width_left+1,y,2))
        map_list[(x)*62+number]=' '
    if open_list[1]==1:
        if height_up>= x-2:
            number = height_up+1
        else:
            number = random.choice(xrange(height_up+1,x,2))
        map_list[y+(number)*62] =' '
    if open_list[2]==1:
        if y >= width_right-2:
            number = y+1
        else:
            number = random.choice(xrange(y+1,width_right,2))
        map_list[(x)*62+number] =' '
    if open_list[3]==1:
        if x >= height_down-2:
            number = x+1
        else:
            number = random.choice(xrange(x+1,height_down,2))
        map_list[y+(number)*62] =' '
    time.sleep(0.1)
    map_flush()
#    os.system('/usr/bin/clear')
#    map_str = ''
#    for i in map_list:
#        map_str += i
#    print map_str
    map_fenge(height_up,x,width_left,y)
    map_fenge(x,height_down,width_left,y)
    map_fenge(x,height_down,y,width_right)
    map_fenge(height_up,x,y,width_right)
map_fenge(0,26,0,60)


#def daoju():
#    global map_list
    
def hero_site():
    global map_list
    map_list[user['site']]=user['icon']%user['name'][0]
    map_flush()

def hero_clean():
    global map_list
    map_list[user['site']]=' '

def move_hero(x):
    if x in 'wasd':
        site_old = user['site']

        if x == 'w':
            site_new = site_old - 62
            if map_list[site_new]==' ':
                hero_clean()
                user['site'] = site_new

        elif x == 'a':
            site_new = site_old - 1
            if map_list[site_new]==' ':
                hero_clean()
                user['site'] = site_new

        elif x == 'd':
            site_new = site_old + 1
            if map_list[site_new]==' ':
                hero_clean()
                user['site'] = site_new

        else:
            site_new = site_old + 62 
            if map_list[site_new]==' ':
                hero_clean()
                user['site'] = site_new

        hero_site()

#def move_hero(x):
#    if x in 'wasd':
#        if x == 'w':
#            hero_clean()
#            user['site']-=62
#            hero_site()
#        elif x == 'a':
#            hero_clean()
#            user['site']-=1
#            hero_site()
#        elif x == 'd':
#            hero_clean()
#            user['site']+=1
#            hero_site()
#        else:
#            hero_clean()
#            user['site']+=62
#            hero_site()

hero_site()
while True:
     x = getch.getch()
     move_hero(x)
