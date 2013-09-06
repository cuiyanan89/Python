# Create your views here.
from blog.models import Post,Replay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
import json

def index(req):
    if req.user.is_authenticated:
        print 'ok'
    posts = Post.objects.all()
    p = Paginator(posts,1)
    page = req.GET.get('page',1)
    contacts = p.page(page)
    return render(req,'index.html',{'contacts':contacts})

def login_view(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(req,user)
            print user
            text = json.dumps({"username":user.username})
            return HttpResponse(text)
    return HttpResponse("")

def logout_view(req):
    if req.user.is_authenticated:
        logout(req)
    return HttpResponseRedirect('/index/')

def show(req,id):
    post = Post.objects.get(id=id)
    replays = post.replay_set.all()
    p = Paginator(replays,1)
    page = req.GET.get('page',1)
    contacts = p.page(page)
    return render(req,'show.html',{'post':post,'contacts':contacts})

def addreplay(req,id):
    post = Post.objects.get(id=id)
    if req.method == "POST":
        post.replay_set.create(content=req.POST['content'])
    return HttpResponseRedirect('/show/%s'%id)

def addpost(req):
    user = req.user
    if req.method == "POST":
        user.post_set.create(title=req.POST['title'],content=req.POST['content'])
    return HttpResponseRedirect('/index/')
