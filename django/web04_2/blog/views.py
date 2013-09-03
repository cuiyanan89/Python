# Create your views here.
from django.shortcuts import render_to_response
from blog.models import picture

def index(req):
    pic = picture.objects.all()
    return render_to_response('index.html',{"pic":pic})
def disp_pic(req,pic_id,pic_name):
#    id = req.GET['id']
    print pic_id,pic_name
    pic = picture.objects.get(id=pic_id)
    return render_to_response('disp_pic.html',{'id':pic_id,'pic':pic})

def show(req,template_name):
    return render_to_response(template_name,{"date":'test'})
