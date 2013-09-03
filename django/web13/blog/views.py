#coding:utf8
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django import forms
from blog.models import User
import hashlib
from django.forms import Textarea
from django.core.exceptions import ObjectDoesNotExist

class UserForm(forms.ModelForm):
#    re_password = forms.CharField(widget=forms.PasswordInput,label=u"再次输入口令")
    class Meta:
        model = User
#        fields = ('username','password','email','birthday','headimg','desc')
#        fields = ('username','password','disc')
        fields = ('username','password')
        widgets = {
            'password':forms.PasswordInput,
#            'disc': Textarea(attrs={'cols':80,'rows':20}),
            }

def register(req):
    if req.method == "POST":
        uf = UserForm(req.POST,req.FILES)
        if uf.is_valid():
            uf.instance.password = hashlib.sha1(uf.cleaned_data['password']).hexdigest()
#            print uf.instance.password
#            uf.cleaned_data['password'] = hashlib.md5(uf.cleaned_data['password']).hexdigest()
            uf.save()
            return HttpResponseRedirect('/login/')

    else:
        uf = UserForm()

    return render(req,'register.html',{'uf':uf})


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST,req.FILES)
        if uf.is_valid():
            password = hashlib.sha1(uf.cleaned_data['password']).hexdigest()
            username = uf.cleaned_data['username']
            try:
                User.objects.get(username=username,password=password)
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username',value=username,max_age=300)
                return response
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/register/')
    else:
        uf = UserForm()
    return render(req,'login.html',{'uf':uf})

def index(req):
    try:
        return HttpResponse('welcome %s'%req.COOKIES['username'])
    except:
        return HttpResponseRedirect('/login/')
