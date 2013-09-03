# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from blog.models import Employ
from django import forms
from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate,login,logout

class RegistForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    tel = forms.CharField()
    headimg = forms.FileField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

def regist(req):
    if req.method == "POST":
        uf = RegistForm(req.POST,req.FILES)
        print uf.is_valid()
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            tel = uf.cleaned_data['tel']
            headimg =uf.cleaned_data['headimg']
            user = User.objects.create_user(username=username,password=password)
            user.is_staff = True
            employ = Employ.objects.create(user=user,tel=tel,headimg=headimg)

            return HttpResponseRedirect('/login/')
    else:
        uf = RegistForm()
    return render(req,'regist.html',{'uf':uf})

def userlogin(req):
    if req.method == "POST":
        rf = LoginForm(req.POST)
        if rf.is_valid():
            user = authenticate(username=rf.cleaned_data['username'],password=rf.cleaned_data['password'])
            print user
            if user:
                login(req,user)
#                return HttpResponseRedirect('/show/')
#                return HttpResponseRedirect('/index/')
#                return HttpResponse('ok')
                return HttpResponse('%s'%user.username)
    else:
        rf = LoginForm()
    return render(req,'login.html',{'rf':rf})

def show(req):
    if req.user.is_authenticated():
        user = req.user
        if user:
            return render_to_response('show.html',{'user':user})
    return HttpResponseRedirect('/login/')



def index(req):
    user = None
    if req.user.is_authenticated():
        user = req.user
    return render(req,'index.html',{'user':user})


def userlogout(req):
    if req.user.is_authenticated():
        user = req.user
        logout(req)
    return HttpResponseRedirect('/index/')
