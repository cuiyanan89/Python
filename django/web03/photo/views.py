# Create your views here.
#coding:utf-8
from django.shortcuts import render_to_response
from photo.models import Picture
import os
import os.path

def show(req):
    s = os.listdir(os.path.join(os.getcwd(),'upload'))
    c = {}
    c['pic'] = s
    print c
    pic_list = Picture.objects.all()
    return render_to_response('show.html',{'title':'相册','pic_list':pic_list})
