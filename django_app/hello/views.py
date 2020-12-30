from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import UserForm
from .models import Person

# Create your views here.

def index(request):
    data = Person.objects.all()
    params = {
        'title': 'Hello',
        'msg': 'your data',
        'form': UserForm(),
        'data' : data
    }

    return render(request, 'hello/index.html', params)

def edit(request, num):
    obj = Person.objects.get(id=num)
    if request.method == 'POST':
        user = UserForm(request.POST, instance=obj) 
        user.save()
        return redirect(to='/hello') 

    params = {
        'title': 'edit',
        'id' : num,
        'form' : UserForm(instance=obj)
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    user = Person.objects.get(id=num)

    if request.method == 'POST':
        user.delete()
        return redirect(to='/hello') 

    params = {
        'title': 'delete',
        'id' : num,
        'form' : user
    }
    
    return render(request, 'hello/delete.html', params)

def create(request):
    params = {
        'title': 'Hello',
        'form': UserForm(),
    }

    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        age = request.POST['age']

        person = Person(name=name, mail=mail, age=age)
        person.save()
        return redirect(to='/hello')

    return render(request, 'hello/index.html', params)

