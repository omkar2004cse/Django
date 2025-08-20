from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world. you are at Django Home page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello you are at Django About page")

def contact(request):
    return HttpResponse("hello. you are in Django contact page")