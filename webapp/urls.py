from django.urls import path
from webapp import views

urlpatterns = [
     path('', views.home, name='index-page'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('products/', views.products, name='products'),
     path('client/', views.client, name='client'),
     path('login/', views.loginPage, name="login"),
     path('client/<str:pk_test>/', views.client, name="client"),
     path('register/', views.registerPage, name="register"),
     path('create_order/<str:pk>/', views.createOrder, name="create_order"),
     path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
     path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
     ]