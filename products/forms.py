from django import forms
from .models import Products, ProductComment, Hashtag
class ProductForm(forms.ModelForm):
    hashtags= forms.CharField( required=False, help_text="해쉬태그를 쉼표로 구분해서 입력하세요")
    class Meta:
        model = Products
        fields =[
            'title',
            'content',
            'product_image',
            'hashtags'
            ]
        
    
    def clean_hashtags(self):
        hashtags = self.cleaned_data['hashtags']
        hashtag_list = [tag.strip() for tag in hashtags.split(',')]
        for tag in hashtag_list:
            if not tag.isalnum():  # 특수문자 및 공백 검증
                raise forms.ValidationError("해시태그는 공백이나 특수문자를 포함할 수 없습니다.")
        return hashtag_list
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields =[
            'comment',
        ]
        