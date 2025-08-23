from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello world. you are at Django Home page")
    return render(request,'project/index.html')

def about(request):
    # return HttpResponse("Hello you are at Django About page")
    return render(request,'project/about.html')

def contact(request):
    # return HttpResponse("hello. you are in Django contact page")
    return render(request,'project/contact.html')