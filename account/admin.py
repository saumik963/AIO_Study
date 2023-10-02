from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class CustomUserAdmin(UserAdmin):
    model = UserProfile
    # Customize the fields you want to display in the list view
    list_display = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'bio', 'dp')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    # Add fields you want to be searchable
    search_fields = ('username', 'email', )


admin.site.register(UserProfile, CustomUserAdmin)
