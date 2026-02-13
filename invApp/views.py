from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# CRUD routes
# Create your views here.

#Home View

def home_view(request):
    return render(request, 'home.html')

#Create View

def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('productlist')
    return render(request,'productform.html',{'form':form}) #if request is not a POST/submission, we just go back to the empty form template view

#Read View

def read_view(request):
    products = Product.objects.all()
    return render(request,'productlist.html',{'products':products})

#Update View

def update_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method=='POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('productlist')
    return render(request,'productform.html',{'form':form})

#Delete View

def delete_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('productlist')
    return render(request,'confirmdelete.html',{'product':product})