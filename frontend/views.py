# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

def home(request):
    return render_to_response('home.html', locals(), RequestContext(request))



