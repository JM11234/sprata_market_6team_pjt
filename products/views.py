from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CommentForm
from .models import Products
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from hitcount.views import HitCountDetailView


class ProductDetailView(HitCountDetailView):
    model = Products
    template_name = 'products/detail.html'
    count_hit = True
    
# Create your views here.
def index(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "products/index.html", context)

@login_required
def create(request):
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author =request.user
            product.save()
            return redirect("index")
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request,'products/create.html',context)    

def detail(request,pk):
    product = get_object_or_404(Products,id=pk)
    form = CommentForm()
    context ={
        "product":product,
        "form":form,
    }
    return render(request, 'products/detail.html', context)

@require_POST
def delete(request,pk):
    product = get_object_or_404(Products,id=pk)
    if request.user.is_authenticated:
        if request.user == product.author:
            product.delete()
    return redirect('index')

@require_http_methods(["GET","POST"])
def update(request,pk):
    product = get_object_or_404(Products,id=pk)
    
    if request.method=="POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'product':product,
        'form':form
    }
    return render(request,'products/update.html',context)