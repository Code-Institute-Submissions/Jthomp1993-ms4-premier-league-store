# Generated by Django 3.1.7 on 2021-04-27 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='products',
            new_name='product',
        ),
    ]
