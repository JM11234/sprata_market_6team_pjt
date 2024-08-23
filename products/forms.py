from django import forms
from .models import Products, ProductComment, Hashtag

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
        
# class HashtagForm(forms.ModelForm):
#     class Meta:
#         model = Hashtag