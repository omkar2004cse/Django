from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tweet(request):
    return render(request,'app.html')
