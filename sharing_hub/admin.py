from django.contrib import admin

from sharing_hub.models import Share


# Register your models here.
@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ("user", "file", "created_at", "updated_at")
    search_fields = ("file", "created_at", "updated_at")
    ordering = ("created_at",)
