from django.urls import path
from store import views
from store.views import (ProductListView, ShopView,CategoryProductsView,AllCategoriesView,
                         DiscountedProductsView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView,WishlistView,ToggleWishlistView)

app_name = 'store'  

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/', ShopView.as_view(), name='shop'),
    path('categories/', AllCategoriesView.as_view(), name='all_categories'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('sales/', DiscountedProductsView.as_view(), name='discounted_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('adding/', ProductCreateView.as_view(), name='adding'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/toggle/<int:pk>/', ToggleWishlistView.as_view(), name='toggle_wishlist'),
]
