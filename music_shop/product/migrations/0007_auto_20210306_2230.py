# Generated by Django 3.1.6 on 2021-03-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210306_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='imageurl',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
