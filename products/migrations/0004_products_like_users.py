# Generated by Django 5.1 on 2024-08-23 00:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_content_productcomment_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='like_users',
            field=models.ManyToManyField(related_name='like_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
