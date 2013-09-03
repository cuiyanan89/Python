# Create your views here.
from django.shortcuts import render_to_response
from blog.models import picture

def index(req):
    return render_to_response('index.html',{'picture_list':picture.objects.all})
