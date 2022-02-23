from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('WELCOMW TO BROTHERHOOD from ' + request.META['REMOTE_ADDR'])
