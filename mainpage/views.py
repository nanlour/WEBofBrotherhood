from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'ip': request.META['REMOTE_ADDR']}
    return render(request, 'mainpage/index.html', context=context)
