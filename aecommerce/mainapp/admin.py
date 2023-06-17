from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    CategoryModel,
    ProductModel,
    ProductImageModel
)


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin, object):
    prepopulated_fields = {
        'slug': [
            'name'
        ]
    }


@admin.register(ProductModel)
class ProductAdmin(ModelAdmin, object):
    prepopulated_fields = {
        'slug': [
            'name'
        ]
    }


@admin.register(ProductImageModel)
class ProductImageAdmin(ModelAdmin, object):
    pass
