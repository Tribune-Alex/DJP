from django.urls import path
from store import views

app_name = 'store'  

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.shop, name='shop'),
    path('categories/', views.all_categories, name='all_categories'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('sales/', views.discounted_products, name='discounted_products'),
    path('product/<int:product_pk>/', views.detail, name='detail'),
    path('adding/',views.adding, name='adding'),
    path('update/<int:product_pk>/',views.update, name='update'),
    path('delete/<int:product_pk>/',views.delete, name='delete'),
]
