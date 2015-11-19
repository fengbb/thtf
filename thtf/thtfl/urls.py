from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginsesion.views.home', name='home'),
    # url(r'^loginsesion/', include('loginsesion.foo.urls')),
    # Unomment the next line to enable the admin:
    #url(r'^comment/(\d{0,10})/$',  TemplateView.as_view(template_name='comment.html')),
    url(r'^regist/$', views.regist),
    #url(r'^$', 'blog.views.login_view', name="home"),
)
