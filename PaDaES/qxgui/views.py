# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import HttpResponseRedirect

def index(request):
    redirect_url = '/static/padaes/%s/index.html'
    if settings.DEBUG:
        redirect_url = redirect_url % ('source')
    else:
        redirect_url = redirect_url % ('build')
    return HttpResponseRedirect(redirect_url)
