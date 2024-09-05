from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', blank=True, default="static/image/default_profile.png")