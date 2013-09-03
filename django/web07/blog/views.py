# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import new

def upload(req):
    if req.method=='POST':
        img = req.FILES['img']
        s = img.read()
        new.objects.create(title=req.POST['title'],content=req.POST['content'],img=img)
        return HttpResponse('<pre>%s</pre>'%s)
    else :
        return render(req,'upload.html',{})
