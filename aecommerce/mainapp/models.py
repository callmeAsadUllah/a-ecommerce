import uuid
from django.db import models
from django.db.models import Model


class CategoryModel(Model, object):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(
        verbose_name='image',
        name='image',
        upload_to='category'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=255,
        unique=True
    )

    def __str__(self) -> str:
        return f'{self.name}'


class ProductModel(Model, object):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='product'
    )

    def __str__(self) -> str:
        return f'{self.name}'


class ProductImageModel(Model, object):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(
        verbose_name='image',
        name='image',
        upload_to='image\product\%y\%m\%d',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='product_images',
        related_query_name='product_image'
    )

    def __str__(self) -> str:
        return f'{self.image} for {self.product.name}'


