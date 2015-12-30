# -*- coding: utf-8 -*-

from django.http import *
from django.template.context_processors import csrf

def default(request):

    return HttpResponse("Ben hayri")