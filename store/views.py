from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Count
from .models import Product, Category
from store.forms import Add_product


def home(request):
    
    products = Product.objects.filter(
        is_available=True
    ).order_by('price').select_related('category')
    
    
    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    quantity = Product.objects.all()
    
    
    featured_products = Product.objects.filter(
        is_available=True,
        is_discounted=True
    ).select_related('category')[:5]  

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'quantity': quantity,
        'featured_products': featured_products
    })

def shop(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by('price').select_related('category')
    
    
    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    quantity = Product.objects.all()
    
    
    featured_products = Product.objects.filter(
        is_available=True,
        is_discounted=True
    ).select_related('category')[:5]  

    return render(request, 'shop.html', {
        'products': products,
        'categories': categories,
        'quantity': quantity,
        'featured_products': featured_products
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(is_available=True).select_related('category')

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })

def all_categories(request):
    categories = Category.objects.all()

    return render(request, 'all_categories.html', {
        'categories': categories
    })


def discounted_products(request):
    products = Product.objects.filter(
        is_discounted=True,
        is_available=True
    ).select_related('category')

    return render(request, 'discounted_products.html', {
        'products': products
    })


def detail(request, product_pk):
    product = get_object_or_404(Product.objects.select_related('category'), pk=product_pk)
    return render(request, 'detail.html', {'product': product})

def adding(request):

    if request.method == "POST":
        form=Add_product(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store:all_categories')
    
    else:
        form=Add_product()

    return render(request, 'adding.html', {'form':form})

def update(request, product_pk):
    product = get_object_or_404(Product,pk=product_pk)

    if request.method == "POST":
        form=Add_product(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('store:detail', product_pk=product_pk)
    
    else:
        form=Add_product(instance=product)

    return render(request, 'update.html', {'form':form})



def delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        product.delete()
        return redirect('store:home')

    return redirect('store:detail', product_pk=product_pk)