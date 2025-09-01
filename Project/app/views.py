from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'app/app.html')
def d(request):
    return render(request, 'd/d.html')