# Create your views here.
#coding:utf-8
from blog.models import Nav,New
from django.shortcuts import render_to_response
def index(req):
    crumbs = ['首页']
    nav_list = Nav.objects.all()
    new_list = []
    for nav in nav_list:
        nav = nav.new_set.all()
        if len(nav) > 0:
            new_list.append(nav[0])
    print new_list

    return render_to_response('index.html',{'nav_list':nav_list,'crumbs':crumbs,'new_list':new_list})


def disp_nav(req,nav_id):
    nav_list = Nav.objects.all()
    nav = Nav.objects.get(id__exact=nav_id)
    crumbs = ['首页>']
    crumbs.append(nav)
    new_list = nav.new_set
    return render_to_response('nav.html',{'nav':nav,'nav_list':nav_list,'crumbs':crumbs})

def disp_new(req,new_id):
    nav_list = Nav.objects.all()
    new = New.objects.get(id__exact=new_id)
    crumbs = ['首页>']
    crumbs.append(str(new.nav)+'>')
    crumbs.append('正文')
    return render_to_response('new.html',{'new':new,'nav_list':nav_list,'crumbs':crumbs})
