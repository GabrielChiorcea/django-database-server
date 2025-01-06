from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    return HttpResponse("You're looking at question.")
# Create your views here.
