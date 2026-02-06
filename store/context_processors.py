from .models import Category,Product
from django.db.models import Count

def categories_processor(request):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    return {'navbar_categories': categories}


def latest_products(request):
    return {
        'latest_products': Product.objects.order_by('-id')[:5]
    }

