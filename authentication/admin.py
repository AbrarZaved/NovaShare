from django.contrib import admin
from django.contrib.auth.models import Group

from authentication.models import User

# Register your models here.
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

