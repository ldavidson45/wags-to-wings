from django.db import models

# Create your models here.
class Order(models.Model):
  order_status: models.CharField(max_length=50)

class Cart(models.Model):
  order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='cart')
  browser_id = models.CharField(max_length=50)

class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.TextField()
  image_url = models.CharField(max_length=300)
  animal_type = models.CharField(max_length=20)

class Cart_Item(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
  quantity = models.IntegerField()
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

class Shipping_Detail(models.Model):
  name = models.CharField(max_length=100)
  address = models.TextField()
  credit_card_number = models.CharField(max_length=20)
  order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_detail')