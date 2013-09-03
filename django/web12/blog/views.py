# Create your views here.
#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import User
from blog.form import UserForm
import hashlib

#class UserForm(forms.Form):
#    username = forms.CharField(max_length=30,label=u"姓名")
#    password = forms.CharField(min_length=6,widget=forms.PasswordInput,label=u"密码")
#    email = forms.EmailField()
#    birthday = forms.DateField(required=False,label=u"生日")
#    headimg = forms.FileField()
#    desc = forms.CharField(widget=forms.Textarea)
##    sex = forms.ChoiceField(widget=forms.RadioSelect,choices=(('m','male'),('f','famale')),label=u'性别')

def register(req):
    if req.method=="POST":
        uf = UserForm(req.POST,req.FILES)
        if uf.is_valid():
            data = uf.cleaned_data
            data['password'] = hashlib.md5(data['password']).hexdigest()
            print data
            user = User()
            user.username = data['username']
            user.password = data['password']
            user.email = data['email']
            user.birthday = data['birthday']
            user.headimg = data['headimg']
            user.desc = data['desc']
            user.sex = data['sex']
            user.save()
            return HttpResponse('ok')
    else:
        uf = UserForm()
    return render(req,'register.html',{"uf":uf})
