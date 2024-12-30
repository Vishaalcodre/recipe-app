"""
    Django Admin Customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
#For Future purpose
from django.utils.translation import gettext as translate

class UserAdmin(BaseUserAdmin):
    """Custom User Admin"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            translate('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (translate("Important dates"), {'fields': ('last_login',)}),
    )

    readonly_fields = ['last_login']
    add_fieldsets = (
        (None,
         {'classes':('wide',),
          'fields': (
              'email',
              'password1',
              'password2',
               'name',
               'is_active',
               'is_staff',
               'is_superuser'
               )}),
        )

# Register the User model with the UserAdmin class to implement Customization
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)