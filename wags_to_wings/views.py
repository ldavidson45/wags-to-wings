from django.shortcuts import render
from .models import Order, Cart, Product, Cart_Item, Shipping_Detail

# Create your views here.
def product_list(request):
  food_items = Product.objects.filter(category="food")
  toy_items = Product.objects.filter(category="toy")
  return render(request, 'wags_to_wings/product_list.html', {'food_items': food_items, 'toy_items': toy_items})
