from django import forms
from favorite.models import FavoriteProduct


class AddToFavoritesForm(forms.ModelForm):
    class Meta:
        model = FavoriteProduct
        fields = ['product']
        widgets = {
            'product': forms.HiddenInput(),
        }