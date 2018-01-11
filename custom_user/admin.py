from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserAdminCreationForm, CustomUserAdminChangeForm


CustomUser = get_user_model()


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    list_display = ('email', 'admin',)
    list_filter = ('admin', 'staff', 'active',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)



