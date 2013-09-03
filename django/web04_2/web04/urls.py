from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web04.views.home', name='home'),
    # url(r'^web04/', include('web04.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','blog.views.index'),
    url(r'^disp_pic/(?P<pic_id>\d+)/(?P<pic_name>\w+)/','blog.views.disp_pic'),
    url(r'^show/old$','blog.views.show',{'template_name':'old.html'}),
    url(r'^show/new$','blog.views.show',{'template_name':'new.html'}),
)