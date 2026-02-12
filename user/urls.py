from django.urls import path
from user.views import UserRegisterView,UserLoginView,ProfileUpdateView
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns =[
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
]
