import uuid
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


class ProfileModel(Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.ImageField(
        verbose_name='image',
        name='image',
        upload_to='profile'
    )
    is_verified = models.BooleanField(default=False)
    token = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_query_name='profile'
    )

    def __str__(self) -> str:
        return f'{self.user}'




