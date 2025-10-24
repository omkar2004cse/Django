from django.shortcuts import render
from .models import chaiVarity, store
from django.shortcuts import get_object_or_404
from .forms import chai_varity_from


# Create your views here.
def all_chai(request):
    chais = chaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais}) 

def chai_detail(request,chai_id):
    chai=get_object_or_404(chaiVarity,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})

def chai_store_from_view(request):
    stores=None
    if request.method=='post':
        form=chai_varity_from(request.post)
        if form.is_valid():
            chai_variety= form.cleaned_data('chai_varity')
            stores=store.objects.filter(chai_varieties=chai_variety)
    else:
        form=chai_varity_from()
    return render(request,"chai_store.html", {'stores': stores, 'form':form})

def order(request):
    return render(request,'chai/order.html')


