# Generated by Django 3.1.1 on 2020-10-21 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201018_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='salePrice',
        ),
    ]
