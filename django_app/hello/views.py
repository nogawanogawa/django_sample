from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': 'パラメータを埋め込んだページです',
        'goto': 'next'
    }
    return render(request, 'hello/index.html', params)

def form(request):
    email = request.POST['email']
    password = request.POST['password']
    params = {
        'title' : email,
        'msg' : password,
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'Hello/Index',
        'msg': '次のページです',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)
