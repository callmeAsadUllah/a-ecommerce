# Generated by Django 4.2.2 on 2023-06-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_productimagemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product\\%y\\%m\\%d', verbose_name='image'),
        ),
    ]
