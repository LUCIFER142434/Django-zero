from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
from .models import Product


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProductForm()
    return render(request,'form.html',{'form':form})


        