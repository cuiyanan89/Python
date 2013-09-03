# Create your views here.
from django.shortcuts import render,render_to_response
from blog.models import Post
from django.http import HttpResponseRedirect

def post(req):
    posts = Post.objects.all()
    return render_to_response('post.html',{'posts':posts})

def add(req):
    if req.method=="POST":
        title = req.POST['title']
        content = req.POST['content']
        if title !='' and content != '':
            Post.objects.create(title=title,content=content)
        return HttpResponseRedirect('/post')
    else:
        return render(req,'add.html',{})

def show(req,id):
    post = Post.objects.get(id=id)
    if req.method=="GET":
        return render(req,'show.html',{'post':post})
    else:
        if req.POST['func'] == 'update':
            post.title = req.POST['title']
            post.content = req.POST['content']
            post.save()
#            return render(req,'show.html',{'post':post})
            return HttpResponseRedirect('/post')
        elif req.POST['func'] == 'delete':
            post.delete()
            return HttpResponseRedirect('/post')

def replay(req,id):
    post = Post.objects.get(id=id)
    if req.method == "POST":
        if req.POST['func'] == 'replay':
            content = req.POST['content']
            if content != '':
                print content
                post.replay_set.create(content = content)
        else :
            del_replay_id = req.POST['func']
            try:
                post.replay_set.get(id=del_replay_id).delete()
            except:
                pass
    replays = post.replay_set.all()
    return render(req,"replay.html",{'post':post,'replays':replays})
