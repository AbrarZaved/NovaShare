from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class User(AbstractUser):
    groups = None
    user_permissions = None
    pro_pic = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        self.groups=None
        self.user_permissions=None
        super().save(*args, **kwargs)