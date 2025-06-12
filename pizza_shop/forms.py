from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    payment_method = forms.ChoiceField(
        choices=Order.PAYMENT_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Chọn phương thức thanh toán"
    )

    class Meta:
        model = Order
        fields = ['payment_method']
