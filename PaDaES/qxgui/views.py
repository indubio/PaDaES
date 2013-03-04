# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/static/padaes/source/index.html')
