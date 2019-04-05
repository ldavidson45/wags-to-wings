from django.shortcuts import render, redirect
from .models import Order, Cart, Product, Cart_Item, Shipping_Detail
from .forms import ShippingForm

# Create your views here.


def product_list(request):
    food_items = Product.objects.filter(category="food")
    toy_items = Product.objects.filter(category="toy")
    return render(request, 'wags_to_wings/product_list.html', {'food_items': food_items, 'toy_items': toy_items})


def cart_detail(request, browser_id):
    users_cart = Cart.objects.filter(browser_id=browser_id)
    return render(request, 'wags_to_wings/cart_detail.html', {'cart': users_cart})


def create_cart_item(request, pk):
    # this will be a POST method
    print("Create_Cart_Item called.")
    browser_id = request.browser_id
    product_id = request.product.id
    returned_cart, created = Cart.objects.get_or_create(browser_id=browser_id)
    Cart_Item.objects.create(cart=returned_cart.id,
                             product=product_id, quantity=1)
    print("If no error above, cart item was probably created sucessfully")


def delete_cart_item(request, pk):
    print("Delete Cart Item called.")
    Cart_Item.objects.get(id=pk).delete()
    return redirect('cart_detail')


def increase_cart_item(request, pk):
    cart_item_in_question = Cart_Item.objects.get(id=pk)
    cart_item_in_question.quantity += 1
    cart_item_in_question.save()
    print("If no error, cart_item quanitity should have incremented")


def decrement_cart_item(request, pk):
    cart_item_in_question = Cart_Item.objects.get(id=pk)
    cart_item_in_question.quantity -= 1
    cart_item_in_question.save()
    print("If no error, cart_item quanitty should have decremented")


def cart_form(request, self):
    if request.method == "POST":
        form = ShippingForm(request.POST)
        ShippingForm.save(self)
        return redirect('cart_form.html', pk=ShippingForm.pk)
    else:
        form = ShippingForm()
    return render(request, 'wags_to_wings/cart_form.html', {'form': form})


# def create_order(request):
#   if request.method == 'POST':
#     browser_id = request.browser_id
#     # Create order, set status
#     new_order = Order.objects.create(order_status="in process")
#     new_order.save()
#     # Create Shipping_Detail
#     # Update Cart order
