from django import forms
from cart.models import CartItem


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        label="Количество",
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'w-20 p-2 border border-gray-600 rounded-md bg-gray-700 text-white focus:ring-blue-500 focus:border-blue-500',
            'placeholder': '1',
            'min': '1'
        }),
    )
    product_id = forms.IntegerField(widget=forms.HiddenInput())


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'w-20 p-2 border border-gray-600 rounded-md bg-gray-700 text-white focus:ring-blue-500 focus:border-blue-500',
                'min': '1'
            }),
        }