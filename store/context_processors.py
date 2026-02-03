from .models import Category
from django.db.models import Count

def categories_processor(request):
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    return {'navbar_categories': categories}