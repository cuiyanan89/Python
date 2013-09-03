# Create your views here.
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate,login,logout

class RegistForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email')
        widgets = {'password':forms.PasswordInput()}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
def regist(req):
    if req.method == "POST":
        rf = RegistForm(req.POST)
        if rf.is_valid():
            rf.instance.is_staff = True
            rf.instance.set_password(rf.instance.password)
            rf.save()
            return HttpResponse('ok')
    else:
        rf = RegistForm()
        return render(req,'regist.html',{'rf':rf})

def userlogin(req):
    if req.method == "POST":
        rf = LoginForm(req.POST)
        if rf.is_valid():
            user = authenticate(username=rf.cleaned_data['username'],password=rf.cleaned_data['password'])
            if user:
#                req.session['user'] = user
                login(req,user)
                return HttpResponseRedirect('/index/')
    rf = LoginForm()
    return render(req,'login.html',{'rf':rf})
def index(req):
    return render_to_response('index.html',{'user':req.user})
def userlogout(req):
    logout(req)
    return HttpResponseRedirect('/login/')
