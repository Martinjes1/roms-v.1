from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('add_products/', views.addProducts, name='add_products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('allcustomer/',views.all_customer, name='allcustomer'),
    path('update_customer/<str:pk>/', views.UpdateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),
    


]