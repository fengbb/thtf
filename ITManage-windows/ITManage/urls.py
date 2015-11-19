#-*- coding:utf-8 -*-
##定义使用utf-8编码
from django.conf.urls import include, url
from django.contrib import admin
from web import views,api_urls
from web import cus_admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ITManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'session_security/',include('session_security.urls')),
    url(r'^$',views.dashboard),
    url(r'^hosts/$',views.hosts,name='host_list'),
    url(r'^hosts/multi/$',views.hosts_multi),
    url(r'^hosts/crontab/$',views.crontab),
    url(r'^multi_task/log/deatail/(\d+)/$',views.multi_task_log_detail,name='multi_task_log_detail'),
    url(r'^hosts/multi/filetrans$',views.hosts_multi_filetrans),
    url(r'^host/detail/',views.host_detail),
    url(r'^api/',include(api_urls)),
    url(r'^personal/',views.personal,name='personal'),
    url(r'^user_audit/(\d+)/$',views.user_audit,name='user_audit'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^login/$',views.login,name='login'),
    url(r'^accounts/profile/$',views.personal),
]
