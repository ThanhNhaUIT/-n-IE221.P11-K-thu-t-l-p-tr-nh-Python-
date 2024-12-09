# customer/urls.py
from django.urls import path
from . import views

app_name = 'customer' 

urlpatterns = [
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('home/', views.home, name='home'),  # Trang chủ
    path('policy/', views.policy, name='policy'),
    path('about/', views.about, name='about'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
