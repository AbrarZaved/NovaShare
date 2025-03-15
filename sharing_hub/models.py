import random
import string
import uuid
from django.db import models
from django.template.defaultfilters import slugify
from authentication.models import User


class Share(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    file = models.FileField(upload_to="files/", null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        unique_slug = uuid.uuid4().hex[:4]
        if not self.slug:
            self.slug = unique_slug
        super().save(*args, **kwargs)
