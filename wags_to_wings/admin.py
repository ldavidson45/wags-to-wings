from django.contrib import admin
from .models import Order, Cart, Product, Cart_Item, Shipping_Detail

# Register your models here.
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Cart_Item)
admin.site.register(Shipping_Detail)
