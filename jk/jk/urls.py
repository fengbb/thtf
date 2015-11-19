from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'jk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/gethosts.json$','jkl.views.gethosts'),
    url(r'^api/collect$','jkl.views.collect'),
    url(r'^api/test$','jkl.views.postdata'),
    url(r'^admin/', include(admin.site.urls)),
]
