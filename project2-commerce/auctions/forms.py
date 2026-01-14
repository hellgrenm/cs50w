from django import forms
from .models import Category


class NewAuctionForm(forms.Form):
    title = forms.CharField(label="Title", max_length=64)
    description = forms.CharField(label="Description")
    price = forms.DecimalField(
        label="Price",
        max_digits=10,
        decimal_places=2
        )
    
    image_url = forms.URLField(
        label="Image URL",
        required=False
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select category"
    )