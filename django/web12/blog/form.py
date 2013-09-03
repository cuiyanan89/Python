# Create your views here.
#coding:utf8
from django import forms
from django.core.exceptions import ValidationError
import re

num = re.compile(r'^\D+$')
def no_num(value):
    if not re.search(num,value):
        raise ValidationError(u'%s is not a name'%value)


class UserForm(forms.Form):
    username = forms.CharField(max_length=30,label=u"姓名",help_text='xingmingxinxi',validators=[no_num],error_messages={'required':"姓名不得为零"})
    password = forms.CharField(min_length=6,widget=forms.PasswordInput,label=u"密码",error_messages={'min_length':"长度不得小于四位"})
    email = forms.EmailField()
    birthday = forms.DateField(required=False,label=u"生日")
    headimg = forms.FileField()
    desc = forms.CharField(widget=forms.Textarea)
    sex = forms.ChoiceField(initial="m",widget=forms.RadioSelect,choices=(('m','male'),('f','famale')),label=u'性别')
