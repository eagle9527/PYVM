#!/usr/bin/env pytthon
# -*- coding: utf8 -*-
__author__ = 'Eagle'

from  django.shortcuts  import render,HttpResponse

def GetData(request):
    message =  request.POST
    print   "Username: %s  Password: %s" % (request.POST['username'],request.POST['password'])
    return HttpResponse('OK')