from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#Home View
@login_required
def home_view(request):
    return render(request, 'home.html')

#Create View
@login_required
def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invApp:productlist')
    return render(request,'productform.html',{'form':form}) #if request is not a POST/submission, we just go back to the empty form template view

#Read View
@login_required
def read_view(request):
    products = Product.objects.all()
    return render(request,'productlist.html',{'products':products})

#Update View
@login_required
def update_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method=='POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('invApp:productlist')
    return render(request,'productform.html',{'form':form})

#Delete View
@login_required
def delete_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('productlist')
    return render(request,'confirmdelete.html',{'product':product})