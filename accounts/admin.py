from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Employee

admin.site.register(Employee)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Personal info',
            {
                'fields': ('full_name', 'display_name', 'phone_number', 'state', 'user_field')
            }
        ),
        (
            'Permissions',
            {
                'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)
            }
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')})

    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'user_field', 'full_name',
                    'phone_number', 'state', 'display_name'
                ),
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
