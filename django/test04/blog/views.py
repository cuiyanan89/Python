# Create your views here.
from django.shortcuts import render_to_response
from blog.models import picture

def index(req):
    pic_all = picture.objects.all()
    return render_to_response('index.html',{'pic_all':pic_all})
def disp_pic(req,id):
    pic = picture.objects.get(id=id)
    print pic 
    return render_to_response('disp_pic.html',{'pic':pic})
