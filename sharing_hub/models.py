import uuid
from django.db import models
from django.template.defaultfilters import slugify
from authentication.models import User
from sharing_hub.file_handler import encrypt_file, decrypt_file
from django.core.files.base import ContentFile
import os
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
        if self.file:
            original_content = self.file.read()
            encrypted_content = encrypt_file(original_content)
            self.file.save(self.file.name, ContentFile(encrypted_content), save=False)
        super().save(*args, **kwargs)

    def get_decrypted_file(self):
        encrypted_content = self.file.read()
        return decrypt_file(encrypted_content)
