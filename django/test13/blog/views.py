#coding:utf8
# Create your views here.
from django.http import HttpResponseRedirect
import hashlib
from django.shortcuts import render,render_to_response
from blog.form import UserForm
from blog.models import User,Foodtype,Food
from django.core.exceptions import ObjectDoesNotExist
def regist(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            try:
                User.objects.get(username=uf.instance.username)
                uf = UserForm()
                return render(req,'regist.html',{'uf':uf})
            except:
                uf.instance.password = hashlib.sha1(uf.cleaned_data['password']).hexdigest()
                uf.save()
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(req,'regist.html',{'uf':uf})
def login(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.instance.username
            password = hashlib.sha1(uf.cleaned_data['password']).hexdigest()
            try:
                User.objects.get(username=username,password=password)
                response = HttpResponseRedirect('/food/1')
                response.set_cookie('username',value=username)
                return response
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/regist/')
    else:
        uf = UserForm()
    return render(req,'login.html',{'uf':uf})
def food(req,id):
    if not req.COOKIES.has_key('username'):
        return HttpResponseRedirect('/login/')
    username = req.COOKIES['username']
    return_dir = {'username':username}
    if req.method == "POST":
         num = req.POST['num']
         if num > 0:
             if id == 3:
                response = HttpResponseRedirect('/clearing/')
             else:
                food_list = Foodtype.objects.get(id=id+1).food_set.all()
                return_dir['food_list'] = food_list
                response = render(req,'food.html',return_dir)

    food_list = Foodtype.objects.get(id=id).food_set.all()
    return_dir['food_list'] = food_list
    return render(req,'food.html',return_dir)
def clearing(req):
    s = ''
    value = 0
    for key in req.COOKIES.keys:
        s += key+' '
       
def logout(req):
    response = HttpResponseRedirect('/food/1')
    response.delete_cookie('username')
    return response
