#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: forms.py
#Author: xiaobing
#E-mail: xiaobingzhang29@gmail.com
#Date: 2013-11-03
#Description: 

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from appname.models import User

class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        print 'kdkdkdkdkddkdk'
        del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)

class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
