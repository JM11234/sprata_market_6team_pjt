from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CommentForm
from .models import ProductComment, Products, Hashtag
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from datetime import timedelta


# Create your views here.

def index(request):
    query = request.GET.get("query","").strip()
    sort = request.GET.get("sort","")
    products = Products.objects.all()
    if sort == 'likes':
        products = products.annotate(count =Count('like_users')).order_by('-count','-pk')
    else:
        products = products.order_by("-pk")
    if query:
         products = products.filter(Q(title__icontains=query)|Q(content__icontains=query)|Q(hashtag__content__icontains=query)).distinct()
    
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
            hashtags=form.cleaned_data["hashtags"]
            for tag in hashtags:
                # 해쉬태그 중복생성 방지
                hashtag, created =Hashtag.objects.get_or_create(content=tag)
                product.hashtag.add(hashtag)
            return redirect("index")
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request,'products/create.html',context)    


def detail(request,pk):
    product = get_object_or_404(Products,id=pk)
    # 사용자가 이 상품 페이지를 방문했는지 세션에서 확인
    if not request.session.get(f'v_{pk}'):
        product.p_hit += 1
        product.save()
        # 세션에 이 상품을 방문했음 기록
        request.session[f'v_{pk}'] = True

        # 세션 만료 시간 설정 (예: 1일)
        request.session.set_expiry(timedelta(days=1))
        
    comments = product.comments.all().order_by('-pk')
    form = CommentForm()
    context ={
        "product":product,
        "form":form,
        "comments":comments
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
            product=form.save(commit=False)
            product.author =request.user
            product.save()
            product.hashtag.clear()
            hashtags=form.cleaned_data["hashtags"]
            for tag in hashtags:
                # 해쉬태그 중복생성 방지
                hashtag, created =Hashtag.objects.get_or_create(content=tag)
                product.hashtag.add(hashtag)
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'product':product,
        'form':form
    }
    return render(request,'products/update.html',context)

@login_required
def comment_create(request,pk):
    form  = CommentForm(request.POST)
    product = get_object_or_404(Products,id=pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.reviewer = request.user
        comment.goods = product
        comment.save()
        return redirect('products:product_detail', product.pk)

@require_POST   
def comment_delete(request,pk):
    comment = get_object_or_404(ProductComment,id=pk)
    product = comment.goods
    if request.user.is_authenticated:
        if request.user == comment.reviewer:
            comment.delete()
    return redirect('products:product_detail',product.id)

@require_POST
def like(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)  # 좋아요 취소
        else:
            product.like_users.add(request.user)
        return redirect("products:product_detail", product.pk)
    return redirect("accounts:login")
