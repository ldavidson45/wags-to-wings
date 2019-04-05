from django import forms
from .models import Shipping_Detail


class ShippingForm(forms.ModelForm):

    class Meta:
        model = Shipping_Detail
        fields = ("name", "address", "credit_card_number")
