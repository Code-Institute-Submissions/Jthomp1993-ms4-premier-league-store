# Generated by Django 3.1.7 on 2021-04-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20210427_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=150),
        ),
    ]
