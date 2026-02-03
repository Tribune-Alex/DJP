from django.urls import path
from store import views

app_name = 'store'  

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('sales/', views.discounted_products, name='discounted_products'),
    path('product/<int:product_pk>/', views.detail, name='detail'),
]
