from django.contrib import admin
from .models import Products, ProductComment, Hashtag
# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductComment)
class ProductsCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass