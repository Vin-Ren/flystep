
from django.forms import ModelForm
from django import forms

from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "name price description thumbnail category is_featured stock".split()
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input input-bordered input-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter product name...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'input input-bordered input-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter price...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea textarea-bordered textarea-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter product description...',
                'rows': 4
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'input input-bordered input-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter image URL...'
            }),
            'category': forms.TextInput(attrs={
                'class': 'input input-bordered input-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter category...'
            }),
            'is_featured': forms.CheckboxInput(),
            'stock': forms.NumberInput(attrs={
                'class': 'input input-bordered input-lg w-full bg-base-200/50 focus:bg-base-100 transition-colors duration-200',
                'placeholder': 'Enter stock quantity...'
            }),
        }
