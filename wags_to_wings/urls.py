from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart_form', views.cart_form, name='cart_form')
]
