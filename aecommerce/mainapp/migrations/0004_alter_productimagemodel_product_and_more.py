# Generated by Django 4.2.2 on 2023-06-17 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_categorymodel_created_at_categorymodel_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', related_query_name='product_image', to='mainapp.productmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to='mainapp.categorymodel'),
        ),
    ]
