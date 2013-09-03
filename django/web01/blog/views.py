# Create your views here.
from django.http import HttpResponse
import os

def show(req):
    return HttpResponse(req.get_host() +'<br/>'+ req.path+"<br/>"+os.getcwd() +'<br/>hello from blog.views.show')
