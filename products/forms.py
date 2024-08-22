from django import forms
from .models import Products, ProductComment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =[
            'title',
            'content',
            'product_image',
        ]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields =[
            'comment',
        ]
        