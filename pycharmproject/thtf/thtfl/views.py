#-*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
#from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.contrib import auth
from thtfl.forms import UserForm,UserRegistForm
from thtfl.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from gevent import monkey
#monkey.patch_all()
from django import *
#from werkzeug.exceptions import BadRequest,Unauthorized
#import wssh
#from wssh.server import WSSHBridge
import json

#app = django(__name__)
def index(req):
    username = req.session.get('username','anybody')
    return render_to_response('index1.html',{'username':username})
def regist(request):
    if request.method == 'POST':
        urf = UserRegistForm(request.POST)
        #urf = UserRegistForm(request.POST)
        if urf.is_valid():
            user = urf.cleaned_data['username']
            passwd = urf.cleaned_data['password']
            emailaddress = urf.cleaned_data['email']
            print (urf.cleaned_data['username'])
            print (urf.cleaned_data['password'])
            print (urf.cleaned_data['email'])
            User.objects.create(username=user, password=passwd, email=emailaddress)
            return render_to_response('register_success.html')
    else:
        urf = UserRegistForm()
    return render_to_response('regist.html', {'urf': urf})

def login(request):
    if request.method == 'GET':
        request.session['login_form'] =  request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #user = auth.authenticate(username=username, password=password)
            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
                #auth.login(request, user)
                #print request.user
                print(username)
                print(password)
                #####使用session
                #request.session['username'] = username
                response = HttpResponseRedirect('/')
                ####使用cookie
                #response.set_cookie('username',username,3600)
                #lt = loader.get_template('home.html')
                #c = RequestContext(request,{'user':user})
                return response
                #return home(request)
                #return HttpResponse(lt.render(c))
                #return render(request, 'home.html', context_instance=RequestContext(request))
            else:
                #验证失败，暂时不做处理
                return HttpResponseRedirect('/login/')
                #return HttpResponseRedirect("/blog/invalid")
#            user = User.objects.filter(username__exact = username, password__exact = password)
#            if user:
#                req.session['username'] = username
#                return HttpResponseRedirect('/blog')
#            else:
#                return HttpResponseRedirect('/blog/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf})
def shellinabox(request):
    ipaddr = "192.168.40.203"
    shellinabox_port = int(8800)
    #url = 'http://%s:%s' % (ipaddr,shellinabox_port)
    url =  'https://%s:%s' % (ipaddr,shellinabox_port)
   # return HttpResponseRedirect(url)
   # username = 'root'
    #password = 'Abcd1234'
    #boxInfo = {'url':url, 'username':username, 'password':password}
    return HttpResponseRedirect(url)



