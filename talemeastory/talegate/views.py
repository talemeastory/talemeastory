from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello, This is Edwin and Sergios multimillion dollar idea <3')
