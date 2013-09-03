# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User
import time
import hashlib

def register(req):
    if req.method=='POST':
#        passtime = time.strftime("%Y-%m-%d %I:%M:%S",time.localtime())
#        print passtime
        try:
            User.objects.get(username=req.POST['username'])
        except:
            birthday = req.POST['birthday']
            if birthday=='':
                birthday = '1970-01-01'
            User.objects.create(username=req.POST['username'],password=hashlib.md5(req.POST['password']).hexdigest(),birthday=birthday,sex=req.POST['sex'],regist_time=time.ctime())
            return HttpResponse('ok ,user %s you registed<br/><a href="/login/">login</a>'%req.POST['username'])

    return render(req,'register.html',{})

def login(req):
    if req.method=="POST":
        try:
            if User.objects.get(username=req.POST['username']).password == hashlib.md5(req.POST['password']).hexdigest():
                return HttpResponse('ok,user %s login'%req.POST['username'])
        except:
            pass
    
    return render(req,'login.html',{})
