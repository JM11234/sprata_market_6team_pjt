from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=50, unique=True, blank=True)
    def __str__(self):
        return self.content
    
class Products(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="uploader")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='default_product.png')
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name = "like_products")
    p_hit = models.PositiveIntegerField(default=0)
    hashtag = models.ManyToManyField(to=Hashtag, related_name="product" )


class ProductComment(models.Model):
    reviewer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commenter"
        )
    goods = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

