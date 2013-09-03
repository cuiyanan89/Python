from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test16.views.home', name='home'),
    # url(r'^test16/', include('test16.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(\d*)$','blog.views.index_view'),
    url(r'^regist/$','blog.views.regist_view'),
    url(r'^login/$','blog.views.login_view'),
    url(r'^logout/$','blog.views.logout_view'),
    url(r'^choose/(\d+)$','blog.views.choose'),
    url(r'^clearing/$','blog.views.clearing'),
    url(r'^confirm/$','blog.views.confirm'),
    url(r'^cleancart/$','blog.views.cleancart'),
)
