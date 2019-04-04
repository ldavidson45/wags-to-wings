from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.TextField()
  image_url = models.CharField(max_length=300)

class Cart_Item(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name=')
  quantity = models.IntegerField()
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

class Cart(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cars')
