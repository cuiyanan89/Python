# Create your views here.
#coding:utf-8
#from django.http import HttpResponse
#from django.template import loader,Context
from django.shortcuts import render_to_response
import os
import os.path

def index(req):
#    t = loader.get_template('index.html')
#    c = Context({"location":os.getcwd(),"path":req.path})
#    c.push()#将c用作堆栈
#    c['title'] = '模板测试'
#    s = t.render(c)
#    return HttpResponse(s)
    c = {'location':os.getcwd(),"path":req.path,"title":"render_to_responser from django.shortcuts"}
    c['goods_list']=['dog','cat','computer']
    c['ss']={'baidu':"http://www.baidu.com","sina":'http://www.sina.com.cn',"google":"http://www.google.com.hk"}
    c['jpg']=[]
    print os.listdir(os.path.join(os.path.split(os.path.abspath(__file__))[0],'static/images'))
    sourse = os.listdir(os.getcwd()+"/blog/static/images")
    for i in sourse:
        if '.jpg' in i:
            c['jpg'].append(os.path.join('/static/images/',i))
    return render_to_response('index.html',c)
