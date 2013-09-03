# Create your views here.
from django.shortcuts import render
from blog.models import New

def new(req):
    if req.method=='POST':
        img = req.FILES['img']
        New.objects.create(new_title=req.POST['title'],new_content=req.POST['content'],new_img=img)
    
    news = New.objects.all()
    return render(req,'new.html',{'news':news})
