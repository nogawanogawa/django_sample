from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if 'test' in request.GET:
        test_query = request.GET['test']
        result = "Query is " + test_query
    else:
        result = "No query parameter"
    return HttpResponse(result)

