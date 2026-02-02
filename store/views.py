from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Product, Category


def home(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by('price')

    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(is_available=True)

    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })


def discounted_products(request):
    products = Product.objects.filter(
        is_discounted=True,
        is_available=True
    )

    return render(request, 'discounted_products.html', {
        'products': products
    })
