from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    context = {'ip': request.META['REMOTE_ADDR']}
    return render(request, 'mainpage/test.html', context=context)

def index(request):
    return render(request, 'mainpage/index.html')

def undone(request):
    return render(request, 'mainpage/undone.html')

def gods(request):
    return render(request, 'mainpage/gods.html')
