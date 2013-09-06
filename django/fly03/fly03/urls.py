from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fly03.views.home', name='home'),
    # url(r'^fly03/', include('fly03.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','blog.views.index'),
    url(r'^login/$','blog.views.login_view'),
    url(r'^logout/$','blog.views.logout_view'),
    url(r'^show/(?P<id>\d*)','blog.views.show'),
    url(r'^addreplay/(?P<id>\d*)$',"blog.views.addreplay"),
    url(r'^addpost/$','blog.views.addpost'),
)
