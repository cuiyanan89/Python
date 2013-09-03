from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.http import HttpResponse
import os.path

def f1(req):
    file = open('/home/yanan/w12/web01/web01/a.txt','r')
    txt = file.read()
    txt = txt.join(['<h3>','<h3>'])
    txt = '</h3><h3>'.join(txt.split('\n'))
    cwd = os.getcwd()
    return HttpResponse(cwd + txt)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web01.views.home', name='home'),
    # url(r'^web01/', include('web01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',f1),
    url(r'^show/$','blog.views.show'),
)
