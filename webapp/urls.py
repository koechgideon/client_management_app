from django.urls import path
from webapp import views

urlpatterns = [
     path('', views.home, name='index-page'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('products/', views.products, name='products'),
     path('customer/', views.customer, name='customer'),
     path('login/', views.loginPage, name="login")
     ]