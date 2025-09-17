from django.shortcuts import render
from .models import chaivarity
# Create your views here.
def app(request):
    chais = chaivarity.objects.all
    return render(request, 'app/app.html',{'chais': chais})
def d(request):
    return render(request, 'd/d.html')