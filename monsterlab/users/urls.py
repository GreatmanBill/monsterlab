#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: urls.py
#Author: xiaobing
#E-mail: xiaobingzhang29@gmail.com
#Date: 2013-11-03
#Description: 
from django.conf.urls import patterns, include, url
import views 

urlpatterns = patterns('',
    url('^login$',views.login, name='login' ),


