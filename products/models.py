from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount

# Create your models here.
class Products(models.Model, HitCountMixin):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="uploader")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='default_product.png')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name = "like_products")


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
    
# 중계테이블로 사용
# class ProductLike(models.Model):
#     user = models.ForeignKey(
#         to=settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE, related_name="like_products"
#     )
#     product = models.ForeignKey(
#         to=Products, on_delete=models.CASCADE, related_name="like_users"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)