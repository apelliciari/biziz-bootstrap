# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from .models import *


def home(request):

    prime_100_tags = Tags.objects.all().order_by('tag')[0:100]

    return render_to_response('home.html', locals(), RequestContext(request))

def skeleton(request):
    return render_to_response('skeleton.html', locals(), RequestContext(request))


