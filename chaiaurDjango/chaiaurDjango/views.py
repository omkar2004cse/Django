from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome..\nYou are at Chai aur code Home Page")
    return render(request,'web/index.html')
def about(request):
    # return HttpResponse("You are at Django About page")
    return render(request,'web/about.html')
def contact(request):
    # return HttpResponse("Please contact at this Page")
    return render(request,'web/contact.html')