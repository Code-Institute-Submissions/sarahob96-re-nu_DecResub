# Generated by Django 3.2 on 2022-10-24 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_product_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_review',
        ),
    ]
