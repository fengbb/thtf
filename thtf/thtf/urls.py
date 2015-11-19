from django.conf.urls import include, url
from django.contrib import admin
from thtfl.views import index,login,shellinabox

urlpatterns = [
    # Examples:
    # url(r'^$', 'thtf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^login/',  login),
    url(r'^shellinabox/', shellinabox),
    url(r'^thtf/', include('thtfl.urls')),

]
