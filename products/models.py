from django.db import models
from django.conf import settings


class Product(models.Model):
    flavor = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="flavor/", blank=True, default="default/default_product.png")
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )

    def __str__(self):
        return self.title