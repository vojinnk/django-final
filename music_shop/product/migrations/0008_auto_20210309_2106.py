# Generated by Django 3.1.6 on 2021-03-09 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210306_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='productimages', to='product.product'),
        ),
    ]