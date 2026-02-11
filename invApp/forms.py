from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product #tells django we're working with the Product model
        fields = '__all__' #includes all fields from defined model
        labels = {
            'product_id': 'Product ID',
            'product_name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity':'Quantity',
            'supplier': 'Supplier'
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={"placeholder":"eg. 1","class":"form-control"}), # specifies that the product_id field should be rendered as a number input with a placeholder and CSS class for styling
            'product_name': forms.TextInput(attrs={"placeholder":"eg. Laptop","class":"form-control"}),
            'sku': forms.TextInput(attrs={"placeholder":"eg. LPT-001","class":"form-control"}),
            'price': forms.NumberInput(attrs={"placeholder":"eg. 999.99","class":"form-control"}),
            'quantity': forms.NumberInput(attrs={"placeholder":"eg. 10","class":"form-control"}),
            'supplier': forms.TextInput(attrs={"placeholder":"eg. Dell Inc.","class":"form-control"})
        } #used to specify the type of widget that will be used to render each input field