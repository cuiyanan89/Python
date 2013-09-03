# Create your views here.
from django.shortcuts import render_to_response

def index(req):
    return render_to_response('index.html',{"ss":{'http://www.baidu.com':"baidu",'http://www.sina.com.cn':"sina",'http://google.com.hk':"google"}})
