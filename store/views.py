from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Product, Category


def home(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by('price').select_related('category')

    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(is_available=True).select_related('category')

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
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
