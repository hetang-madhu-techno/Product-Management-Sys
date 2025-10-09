from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product               
        fields = '__all__'            

        labels = {                    
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }

        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock Keeping Unit'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price '}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier'}),
        }