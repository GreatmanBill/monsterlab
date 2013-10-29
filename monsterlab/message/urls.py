#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: news/urls.py
#Author: xiaobing
#E-mail: xiaobingzhang29@gmail.com
#Date: 2013-10-28
#Description: 

from django.conf.urls import patterns, include, url
import views 

urlpatterns = patterns('',
    url('^$',views.index, name='index' ),

)
