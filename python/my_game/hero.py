#!/usr/bin/python
#encoding=utf-8
import os,time,random
import getch

message = """  ======================欢迎来到游戏======================
           游戏中会出现20个随机包，打开后有意外惊喜
          游戏规则：a向左 s向下 d向右 w向上 退出请按q
           name:%s life:%s knife:%s equip:%s
  ========================================================"""
l = '#'*61
ll = '\n#'+' '*59+'#'
map_str = l+ll*25+'\n'+l
os.system('/usr/bin/clear')
map_list = list(map_str)
user = {'icon':'\x1b[1;41m\x1b[1;33m%s\x1b[0m','name':'Cuiyanan','life':100,'site':63,'knife':0,'equip':0,'mine':0,'bun':0}
goods = ['knife','equip','mine','bun']
goods_site = []

def map_flush():
    global map_list
    map_str = ''
    os.system('/usr/bin/clear')
    for i in map_list:
        map_str += i
    print message%(user['name'],user['life'],user['knife'],user['equip'])
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
    time.sleep(0.05)
    map_flush()
    map_fenge(height_up,x,width_left,y)
    map_fenge(x,height_down,width_left,y)
    map_fenge(x,height_down,y,width_right)
    map_fenge(height_up,x,y,width_right)

    
def hero_site():
    global map_list
    map_list[user['site']]=user['icon']%user['name'][0]
    map_flush()

def boss_site():
    global map_list
    map_list[len(map_str)-64]='\x1b[1;42m\x1b[1;31mB\x1b[0m'
    map_flush()

def hero_clean():
    global map_list
    map_list[user['site']]=' '

def move_hero(x):
    if x in 'wasd':
        site_old = user['site']

        if x == 'w':
            site_new = site_old - 62
            if map_list[site_new]!='#':
                hero_clean()
                user['site'] = site_new

        elif x == 'a':
            site_new = site_old - 1
            if map_list[site_new]!='#':
                hero_clean()
                user['site'] = site_new

        elif x == 'd':
            site_new = site_old + 1
            if map_list[site_new]!='#':
                hero_clean()
                user['site'] = site_new

        else:
            site_new = site_old + 62 
            if map_list[site_new]!='#':
                hero_clean()
                user['site'] = site_new

        hero_site()


def goods_give():
    global map_list
    global goods_site
    length_map = len(map_str)-1
    goods_number = 0
    while goods_number <=20:
        goods_new = random.randint(64,length_map)
        if map_list[goods_new] == ' ':
            goods_number += 1
            goods_site.append(goods_new)
            map_list[goods_new] = '\x1b[1;46m\x1b[1;37mx\x1b[0m'
    map_flush()

def goods_if():
    global goods
    if user['site'] in goods_site:
        goods_site.remove(user['site'])
        good_x = random.randint(0,3)
        good_get = goods[good_x]
        user[good_get] += 1
        if good_get == 'bun':
            user['life'] += 15
        if good_get == 'mine':
            user['life'] -= 15
            if user['life'] <= 0:
                user['life'] == 0
        map_flush()
        print 'you got a %s' % good_get
        time.sleep(0.5)
        

x = raw_input('请输入您的姓名---->')
if len(x)>0:
    user['name']=x

map_fenge(0,26,0,60)
boss_site()
goods_give()
hero_site()
while True:
    x = getch.getch()
    if x == 'q':
        break
    move_hero(x)
    goods_if()
    if user['life'] == 0:
        break
