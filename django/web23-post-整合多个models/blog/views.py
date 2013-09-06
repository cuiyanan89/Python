from blog.models import ProUser
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,login,logout

class RegistForm(forms.ModelForm):
    username=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=('username','password')
        widgets={'password':forms.PasswordInput()}

class ProForm(forms.ModelForm):
    class Meta:
        model=ProUser
        fields=('tel','headimg')

def register(req):
    if req.method=='POST':
        uf=RegistForm(req.POST,req.FILES)
        puf=ProForm(req.POST,req.FILES)
        if uf.is_valid() and puf.is_valid():
            uf.instance.set_password(uf.cleaned_data['password'])
            uf.save()
            puf.instance.user=uf.instance
            puf.save()
            return HttpResponse('hello ok')
    else:
        uf=RegistForm()
        puf=ProForm()
    return render(req,'register.html',{'uf':uf,'puf':puf})

def index(req):
    if req.user.is_authenticated():
        #print req.user
        return render_to_response('login.html',{'user':req.user})
    else:
        return render(req,'login.html',{})

def login_user(req):
    username=req.POST.get('username')
    password=req.POST.get('password')
    #print username,password
    user=authenticate(username=username,password=password)
    if user is not None:
        login(req,user)
        return HttpResponse('%s'%username)
    else:
        return HttpResponse('aaa')
