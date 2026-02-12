from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Count
from .models import Product, Category
from store.forms import Add_product
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
    
#     products = Product.objects.filter(
#         is_available=True
#     ).order_by('price').select_related('category')
    
    
#     categories = Category.objects.annotate(
#         product_count=Count('products')
#     ).filter(product_count__gt=0)

#     quantity = Product.objects.all()
    
    
#     featured_products = Product.objects.filter(
#         is_available=True,
#         is_discounted=True
#     ).select_related('category')[:5]  

#     return render(request, 'home.html', {
#         'products': products,
#         'categories': categories,
#         'quantity': quantity,
#         'featured_products': featured_products
#     })

# def shop(request):
#     products = Product.objects.filter(
#         is_available=True
#     ).order_by('price').select_related('category')
    
    
#     categories = Category.objects.annotate(
#         product_count=Count('products')
#     ).filter(product_count__gt=0)

#     quantity = Product.objects.all()
    
    
#     featured_products = Product.objects.filter(
#         is_available=True,
#         is_discounted=True
#     ).select_related('category')[:5]  

#     return render(request, 'shop.html', {
#         'products': products,
#         'categories': categories,
#         'quantity': quantity,
#         'featured_products': featured_products
#     })


# def category_products(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = category.products.filter(is_available=True).select_related('category')

#     return render(request, 'category_products.html', {
#         'category': category,
#         'products': products
#     })

# def all_categories(request):
#     categories = Category.objects.all()

#     return render(request, 'all_categories.html', {
#         'categories': categories
#     })


# def discounted_products(request):
#     products = Product.objects.filter(
#         is_discounted=True,
#         is_available=True
#     ).select_related('category')

#     return render(request, 'discounted_products.html', {
#         'products': products
#     })


# def detail(request, product_pk):
#     product = get_object_or_404(Product.objects.select_related('category'), pk=product_pk)
#     return render(request, 'detail.html', {'product': product})

# def adding(request):

#     if request.method == "POST":
#         form=Add_product(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('store:all_categories')
    
#     else:
#         form=Add_product()

#     return render(request, 'adding.html', {'form':form})

# def update(request, product_pk):
#     product = get_object_or_404(Product,pk=product_pk)

#     if request.method == "POST":
#         form=Add_product(request.POST, instance=product)

#         if form.is_valid():
#             form.save()
#             return redirect('store:detail', product_pk=product_pk)
    
#     else:
#         form=Add_product(instance=product)

#     return render(request, 'update.html', {'form':form})



# def delete(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)

#     if request.method == 'POST':
#         product.delete()
#         return redirect('store:home')

#     return redirect('store:detail', product_pk=product_pk)

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_available=True)

    def get_queryset(self):
        return (
            Product.objects
            .filter(is_available=True)
            .order_by('price')
            .select_related('category')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['quantity'] = self.get_queryset().count()

        context['categories'] = (
            Category.objects
            .annotate(product_count=Count('products', filter=Q(products__is_available=True)))
            .filter(product_count__gt=0)
        )

        context['featured_products'] = (
            Product.objects
            .filter(is_available=True, is_discounted=True)
            .select_related('category')[:5]
        )

        return context
    

class ShopView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'shop.html'
    queryset = Product.objects.filter(is_available=True)
    context_object_name = 'products'
    login_url=reverse_lazy('user:login')

    def get_queryset(self):
        return (
            Product.objects
            .filter(is_available=True)
            .order_by('price')
            .select_related('category')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = (
            Category.objects
            .annotate(product_count=Count('products',filter=Q(products__is_available=True)))
            .filter(product_count__gt=0)
        )

        context['quantity'] = Product.objects.count()

        context['featured_products'] = (
            Product.objects
            .filter(is_available=True, is_discounted=True)
            .select_related('category')[:5]
        )

        return context
    

class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    queryset = Product.objects.filter(is_available=True)
    context_object_name = 'products'

    def get_queryset(self):
        
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
       
        return self.category.products.filter(is_available=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        
        context['categories'] = (
            Category.objects
            .annotate(product_count=Count('products', filter=Q(products__is_available=True)))
            .filter(product_count__gt=0)
        )
        return context
    
class AllCategoriesView(ListView):
    model = Category
    template_name = 'all_categories.html'
    queryset = Product.objects.filter(is_available=True)
    context_object_name = 'categories'

class DiscountedProductsView(ListView):
    model = Product
    template_name = 'discounted_products.html'
    queryset = Product.objects.filter(is_available=True)
    context_object_name = 'products'

    def get_queryset(self):
        return (
            Product.objects
            .filter(is_discounted=True, is_available=True)
            .select_related('category')
        )
class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    queryset = Product.objects.filter(is_available=True)
    context_object_name = 'product'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = (
            Category.objects
            .annotate(product_count=Count('products', filter=Q(products__is_available=True)))
            .filter(product_count__gt=0)
        )
        return context
    
    
class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = Add_product
    template_name = 'adding.html'
    success_url = reverse_lazy('store:all_categories')
    login_url=reverse_lazy('user:login')

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = Add_product
    queryset = Product.objects.filter(is_available=True)
    template_name = 'update.html'
    login_url=reverse_lazy('user:login')

    def get_success_url(self):
        if not self.object.is_available:
         return reverse_lazy('store:home')
        return reverse_lazy('store:detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('store:home')
    login_url=reverse_lazy('user:login')