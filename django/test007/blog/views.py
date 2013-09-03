# Create your views here.
from django.shortcuts import render,render_to_response
from blog.models import New
from django.http import HttpResponseRedirect

def new(req):
    news = New.objects.all()
    return render_to_response('new.html',{'news':news})

def add(req):
    if req.method == "POST":
        new_title = req.POST['new_title']
        new_content = req.POST['new_content']
        new_img = req.FILES['new_img']
        New.objects.create(new_title=new_title,new_content=new_content,new_img=new_img)
    return render(req,'add.html',{})
