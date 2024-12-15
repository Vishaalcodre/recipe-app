"""
    Django Admin Customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

class UserAdmin(BaseUserAdmin):
    """Custom User Admin"""
    ordering = ['id']
    list_display = ['email', 'name']

# Register the User model with the UserAdmin class to implement Customization
admin.site.register(models.User, UserAdmin)