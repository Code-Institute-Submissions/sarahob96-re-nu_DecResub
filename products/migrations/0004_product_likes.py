# Generated by Django 3.2 on 2022-10-27 22:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='product_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
