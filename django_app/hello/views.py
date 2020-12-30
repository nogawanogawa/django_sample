from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.

def index(request):
    params = {
        'title': 'Hello',
        'msg': 'your data',
        'form': UserForm()
    }
    if request.method == 'POST':
        params['message'] = 'name: ' + request.POST["name"] \
            + "<br> mail: " + request.POST["mail"] \
            + "<br> age: " + request.POST["age"] 
        params["form"] = UserForm(request.POST)

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
