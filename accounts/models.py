from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile/', blank=True, default="default/default_profile.png")