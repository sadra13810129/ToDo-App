from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser','is_active')
    list_filter = ('email', 'is_superuser','is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication',{
            'fields':(
                'email','password'
            ),
        }),
         ('Permossions',{
            'fields':(
                'is_staff','is_active','is_superuser'
            ),
        }),
        ('Group_Permossions',{
            'fields':(
                'groups','user_permissions'
            ),
        }),
        ('Important_Dates',{
            'fields':(
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser", 
            )}
        ),
    )




admin.site.register(User,CustomUserAdmin)
