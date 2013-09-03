# Create your views here.
from django.shortcuts import render_to_response
from blog.models import picture

def index(req):
    pic = picture.objects.all()
    return render_to_response('index.html',{"pic":pic})
def disp_pic(req):
    id = req.GET['id']
    pic = picture.objects.get(id=id)
    return render_to_response('disp_pic.html',{'id':id,'pic':pic})
