# Create your views here.
#form django.shortcuts import render_to_response
from django.http import HttpResponse

def login(req):
    username = req.GET['username']
    sex = req.GET['sex']
    return HttpResponse("welcome %s , sex is %s"%(username,sex))
