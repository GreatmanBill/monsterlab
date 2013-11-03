#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: views.py
#Author: xiaobing
#E-mail: xiaobingzhang29@gmail.com
#Date: 2013-11-03
#Description: 

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.backends import ModelBackend as auth
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
print authenticate.__doc__

def index(request):
    """这是全站的首页"""
    context = {}
    
    return render(request, 'index.html', context)

def login(request, username = None, password = None):
    """该方法用于用户登录
        @param username 用户名
        @param password 密码
    """
    if 'sub' in request.POST:
        #说明用户点击了登录按钮
        username = request.POST['username']
        password = request.POST['password']

    else:
        #说明用户第一次来到登录页面
        context = {}

        return render(request, 'users/login.html', context)
        print 'come here'
    
    user = authenticate(username = username, password = password)
    if user is None:
        #需重新登录
        context = {'error_message':'帐号或密码有误'}

        return render(request, 'users/login.html', context)
    else:
        #登录成功
        print "success"
        context = {}
        return render(request, 'index.html', context)
    

def register():
    pass

def logout():
    pass

def createUser():
    pass

def updateUser():
    pass

def deleteUser():
    pass

def createUserGroup():
    pass

def updateUserGroup():
    pass

def deleteUserGroup():
    pass
 
