from django.contrib import admin

from sharing_hub.models import Share

# Register your models here.
@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
